from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Receipt
from .services import ReceiptService
from .forms import ReceiptUploadForm, ReceiptSearchForm
import logging

logger = logging.getLogger(__name__)

class ReceiptUploadView(View):
    template_name = 'receipts/receipt_upload.html'
    
    def get(self, request):
        form = ReceiptUploadForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = ReceiptUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                receipt = ReceiptService.process_receipt_file(request.FILES['file'])
                messages.success(request, 'Receipt uploaded and processed successfully!')
                return redirect('receipt_detail', pk=receipt.pk)
            except Exception as e:
                messages.error(request, f'Error processing receipt: {str(e)}')
        return render(request, self.template_name, {'form': form})

class ReceiptListView(ListView):
    model = Receipt
    template_name = 'receipts/receipt_list.html'
    context_object_name = 'receipts'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Receipt.objects.filter(is_deleted=False)
        form = ReceiptSearchForm(self.request.GET)
        
        if form.is_valid():
            vendor = form.cleaned_data.get('vendor')
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            min_amount = form.cleaned_data.get('min_amount')
            max_amount = form.cleaned_data.get('max_amount')
            category = form.cleaned_data.get('category')
            search_query = form.cleaned_data.get('search_query')
            
            queryset = ReceiptService.search_receipts(
                query=search_query,
                vendor=vendor,
                start_date=start_date,
                end_date=end_date,
                min_amount=min_amount,
                max_amount=max_amount,
                category=category
            )
        
        sort_by = self.request.GET.get('sort_by', '-transaction_date')
        if sort_by in ['vendor', 'transaction_date', 'amount', 'category']:
            queryset = queryset.order_by(sort_by)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = ReceiptSearchForm(self.request.GET)
        context['sort_by'] = self.request.GET.get('sort_by', '-transaction_date')
        receipts = self.get_queryset()
        context['stats'] = ReceiptService.get_receipt_stats(receipts)
        return context

class ReceiptDetailView(DetailView):
    model = Receipt
    template_name = 'receipts/receipt_detail.html'
    context_object_name = 'receipt'

class ReceiptDeleteView(DeleteView):
    model = Receipt
    context_object_name = 'receipt'
    template_name = 'receipts/receipt_confirm_delete.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Receipt deleted successfully!')
        return reverse_lazy('dashboard')
    
    def get_queryset(self):
        return Receipt.objects.filter(is_deleted=False)

class DashboardView(View):
    template_name = 'receipts/dashboard.html'
    
    def get(self, request):
        receipts = Receipt.objects.filter(is_deleted=False)
        stats = ReceiptService.get_receipt_stats(receipts)
        return render(request, self.template_name, {'stats': stats})