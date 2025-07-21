from django import forms
from .models import Category
from datetime import datetime, timedelta

class ReceiptUploadForm(forms.Form):
    file = forms.FileField(
        label='Receipt File',
        help_text='Upload a receipt (PDF, PNG, JPG, or TXT)'
    )

class ReceiptSearchForm(forms.Form):
    search_query = forms.CharField(
        required=False,
        label='Search Text',
        widget=forms.TextInput(attrs={'placeholder': 'Search in receipt text...'})
    )
    vendor = forms.CharField(
        required=False,
        label='Vendor',
        widget=forms.TextInput(attrs={'placeholder': 'Filter by vendor...'})
    )
    start_date = forms.DateField(
        required=False,
        label='From Date',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    end_date = forms.DateField(
        required=False,
        label='To Date',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    min_amount = forms.DecimalField(
        required=False,
        label='Min Amount',
        min_value=0,
        widget=forms.NumberInput(attrs={'placeholder': 'Minimum amount'})
    )
    max_amount = forms.DecimalField(
        required=False,
        label='Max Amount',
        min_value=0,
        widget=forms.NumberInput(attrs={'placeholder': 'Maximum amount'})
    )
    category = forms.ChoiceField(
        required=False,
        label='Category',
        choices=[('', 'All Categories')] + Category.choices()
    )
    
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        
        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("End date must be after start date.")
        
        min_amount = cleaned_data.get('min_amount')
        max_amount = cleaned_data.get('max_amount')
        
        if min_amount and max_amount and min_amount > max_amount:
            raise forms.ValidationError("Max amount must be greater than min amount.")
        
        return cleaned_data