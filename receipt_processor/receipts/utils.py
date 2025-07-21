import os
import logging
from datetime import datetime, timedelta
from django.conf import settings
from django.core.files.storage import default_storage
from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes
import io

logger = logging.getLogger(__name__)

def clean_extracted_text(text):
    """
    Clean and normalize extracted text from OCR or files.
    """
    if not text:
        return ""
    
    # Remove extra whitespace and normalize line breaks
    text = ' '.join(text.split())
    return text.strip()

def save_uploaded_file(file):
    """
    Save uploaded file to the media directory and return the path.
    """
    try:
        file_name = default_storage.save(f'receipts/{file.name}', file)
        return file_name
    except Exception as e:
        logger.error(f"Error saving file: {e}")
        raise

def is_image_file(file_path):
    """
    Check if the file is an image based on its extension.
    """
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    return os.path.splitext(file_path)[1].lower() in image_extensions

def is_pdf_file(file_path):
    """
    Check if the file is a PDF based on its extension.
    """
    return os.path.splitext(file_path)[1].lower() == '.pdf'

def process_image_for_ocr(image_path):
    """
    Preprocess image to improve OCR accuracy.
    """
    try:
        # Open the image
        img = Image.open(image_path)
        
        # Convert to grayscale
        img = img.convert('L')
        
        # Apply thresholding
        # img = img.point(lambda x: 0 if x < 128 else 255, '1')
        
        return img
    except Exception as e:
        logger.error(f"Error processing image: {e}")
        return None

def extract_text_with_ocr(file_path):
    """
    Extract text from an image file using OCR.
    """
    try:
        if is_image_file(file_path):
            # Preprocess the image
            img = process_image_for_ocr(file_path)
            if img:
                # Use Tesseract to do OCR on the image
                text = pytesseract.image_to_string(img)
                return clean_extracted_text(text)
        
        elif is_pdf_file(file_path):
            # Convert PDF to images and extract text from each page
            with open(file_path, 'rb') as f:
                images = convert_from_bytes(f.read())
            
            text = ""
            for i, image in enumerate(images):
                text += pytesseract.image_to_string(image) + "\n"
            
            return clean_extracted_text(text)
        
        return ""
    except Exception as e:
        logger.error(f"Error in OCR processing: {e}")
        return ""

def calculate_date_range(days=30):
    """
    Calculate date range for filtering (e.g., last 30 days).
    """
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=days)
    return start_date, end_date

def format_currency(amount):
    """
    Format currency amount with proper symbols and decimal places.
    """
    if amount is None:
        return "$0.00"
    return f"${amount:,.2f}"

def get_file_extension(file_name):
    """
    Get the lowercase extension of a file without the dot.
    """
    return os.path.splitext(file_name)[1][1:].lower()

def validate_file_extension(file_name):
    """
    Validate that the file has an allowed extension.
    """
    allowed_extensions = ['pdf', 'png', 'jpg', 'jpeg', 'txt']
    ext = get_file_extension(file_name)
    return ext in allowed_extensions

def get_category_color(category):
    """
    Get a consistent color for each category for UI purposes.
    """
    color_map = {
        'Utilities': 'primary',
        'Groceries': 'success',
        'Entertainment': 'warning',
        'Transportation': 'info',
        'Other': 'secondary'
    }
    return color_map.get(category, 'light')