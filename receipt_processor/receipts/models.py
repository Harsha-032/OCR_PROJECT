from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from enum import Enum

class Category(Enum):
    UTILITIES = "Utilities"
    GROCERIES = "Groceries"
    ENTERTAINMENT = "Entertainment"
    TRANSPORTATION = "Transportation"
    OTHER = "Other"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class Receipt(models.Model):
    file = models.FileField(
        upload_to='receipts/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpg', 'jpeg', 'txt'])]
    )
    vendor = models.CharField(max_length=255)
    transaction_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=Category.choices(), default=Category.OTHER.value)
    extracted_text = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)  # Soft delete field
    
    class Meta:
        ordering = ['-transaction_date']
        indexes = [
            models.Index(fields=['vendor']),
            models.Index(fields=['transaction_date']),
            models.Index(fields=['amount']),
            models.Index(fields=['category']),
            models.Index(fields=['is_deleted']),
        ]
    
    def __str__(self):
        return f"{self.vendor} - {self.transaction_date} - ${self.amount}"
    
    def delete(self, *args, **kwargs):
        """Override delete to handle file deletion"""
        if self.file:
            self.file.delete(save=False)
        super().delete(*args, **kwargs)