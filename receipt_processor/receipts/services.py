from .models import Receipt
from .parsers import extract_text_from_file, parse_receipt
from django.core.exceptions import ValidationError
import logging

logger = logging.getLogger(__name__)

class ReceiptService:
    @staticmethod
    def process_receipt_file(file) -> Receipt:
        """Process uploaded receipt file and create Receipt object."""
        try:
            # Extract text from file
            extracted_text = extract_text_from_file(file)
            if not extracted_text:
                raise ValidationError("Could not extract text from the file.")
            
            # Parse receipt data
            parsed_data = parse_receipt(extracted_text)
            if not parsed_data.get('amount') or not parsed_data.get('transaction_date'):
                raise ValidationError("Could not extract required fields from the receipt.")
            
            # Create and save receipt
            receipt = Receipt(
                file=file,
                vendor=parsed_data['vendor'],
                transaction_date=parsed_data['transaction_date'],
                amount=parsed_data['amount'],
                category=parsed_data['category'],
                extracted_text=parsed_data['extracted_text']
            )
            receipt.save()
            return receipt
        
        except Exception as e:
            logger.error(f"Error processing receipt: {e}")
            raise ValidationError(f"Error processing receipt: {str(e)}")

    @staticmethod
    def search_receipts(query=None, vendor=None, start_date=None, end_date=None, min_amount=None, max_amount=None, category=None):
        """Search receipts with various filters."""
        receipts = Receipt.objects.filter(is_deleted=False)
        
        if query:
            receipts = receipts.filter(extracted_text__icontains=query)
        if vendor:
            receipts = receipts.filter(vendor__icontains=vendor)
        if start_date:
            receipts = receipts.filter(transaction_date__gte=start_date)
        if end_date:
            receipts = receipts.filter(transaction_date__lte=end_date)
        if min_amount:
            receipts = receipts.filter(amount__gte=min_amount)
        if max_amount:
            receipts = receipts.filter(amount__lte=max_amount)
        if category:
            receipts = receipts.filter(category=category)
            
        return receipts

    @staticmethod
    def get_receipt_stats(receipts):
        """Calculate statistics for given receipts."""
        from django.db.models import Sum, Avg, Count
        from django.db.models.functions import TruncMonth
        
        stats = {
            'total_spend': receipts.aggregate(total=Sum('amount'))['total'] or 0,
            'average_spend': receipts.aggregate(avg=Avg('amount'))['avg'] or 0,
            'count': receipts.count(),
            'top_vendors': receipts.values('vendor').annotate(count=Count('id'), total=Sum('amount')).order_by('-total')[:5],
            'monthly_trends': receipts.annotate(month=TruncMonth('transaction_date')).values('month').annotate(total=Sum('amount')).order_by('month'),
            'category_distribution': receipts.values('category').annotate(count=Count('id'), total=Sum('amount')).order_by('-total')
        }
        return stats