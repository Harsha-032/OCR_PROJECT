import re
from datetime import datetime
from dateutil.parser import parse
from typing import Optional, Tuple
import pytesseract
from pdf2image import convert_from_bytes
from PIL import Image
import io
import logging

logger = logging.getLogger(__name__)

VENDOR_KEYWORDS = {
    'amazon': 'Amazon',
    'walmart': 'Walmart',
    'target': 'Target',
    'whole foods': 'Whole Foods',
    'com ed': 'ComEd',
    'at&t': 'AT&T',
    'verizon': 'Verizon',
    'netflix': 'Netflix'
}

CATEGORY_MAPPING = {
    'amazon': 'Groceries',
    'walmart': 'Groceries',
    'target': 'Groceries',
    'whole foods': 'Groceries',
    'com ed': 'Utilities',
    'at&t': 'Utilities',
    'verizon': 'Utilities',
    'netflix': 'Entertainment'
}

def extract_text_from_file(file) -> str:
    """Extract text from various file formats using OCR when needed."""
    try:
        if file.name.lower().endswith('.txt'):
            return file.read().decode('utf-8')
        
        elif file.name.lower().endswith(('.png', '.jpg', '.jpeg')):
            image = Image.open(io.BytesIO(file.read()))
            return pytesseract.image_to_string(image)
        
        elif file.name.lower().endswith('.pdf'):
            images = convert_from_bytes(file.read())
            text = ""
            for image in images:
                text += pytesseract.image_to_string(image) + "\n"
            return text
        
        return ""
    except Exception as e:
        logger.error(f"Error extracting text from file: {e}")
        return ""

def parse_date(text: str) -> Optional[datetime]:
    """Extract date from text using various patterns."""
    date_patterns = [
        r'\d{1,2}/\d{1,2}/\d{2,4}',
        r'\d{1,2}-\d{1,2}-\d{2,4}',
        r'\d{1,2} \w{3,} \d{2,4}',
        r'\w{3,} \d{1,2}, \d{4}',
        r'\d{4}-\d{2}-\d{2}'
    ]
    
    for pattern in date_patterns:
        match = re.search(pattern, text)
        if match:
            try:
                return parse(match.group(), fuzzy=True)
            except:
                continue
    return None

def parse_amount(text: str) -> Optional[float]:
    """Extract amount from text."""
    amount_patterns = [
        r'total\s*:\s*\$?(\d+\.\d{2})',
        r'amount\s*:\s*\$?(\d+\.\d{2})',
        r'\$(\d+\.\d{2})',
        r'(\d+\.\d{2})\s*(usd|dollars)?'
    ]
    
    for pattern in amount_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            try:
                return float(match.group(1))
            except:
                continue
    return None

def parse_vendor(text: str) -> str:
    """Identify vendor from text using keyword matching."""
    text_lower = text.lower()
    for keyword, vendor in VENDOR_KEYWORDS.items():
        if keyword in text_lower:
            return vendor
    return "Unknown Vendor"

def parse_category(vendor: str) -> str:
    """Map vendor to category."""
    vendor_lower = vendor.lower()
    for keyword, category in CATEGORY_MAPPING.items():
        if keyword in vendor_lower:
            return category
    return "Other"

def parse_receipt(text: str) -> dict:
    """Parse receipt text and extract structured data."""
    date = parse_date(text)
    amount = parse_amount(text)
    vendor = parse_vendor(text)
    category = parse_category(vendor)
    
    return {
        'vendor': vendor,
        'transaction_date': date.date() if date else None,
        'amount': amount,
        'category': category,
        'extracted_text': text
    }