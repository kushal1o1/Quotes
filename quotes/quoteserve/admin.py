from django.shortcuts import render
from .forms import CSVUploadForm
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path
from django.contrib import messages
from .models import PreQuote
import csv

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('quote_text', 'author', 'categories')


    # Define the URL for custom CSV upload page
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('upload-csv/', self.upload_csv_view)
        ]
        return custom_urls + urls

    def upload_csv_view(self, request):
        if request.method == "POST":
            form = CSVUploadForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = request.FILES['csv_file']
                try:
                    reader = csv.reader(csv_file.read().decode('utf-8').splitlines())
                    next(reader)  # Skip header
                    for row in reader:
                        quote_text, author, categories = row
                        PreQuote.objects.create(
                            quote_text=quote_text.strip(),
                            author=author.strip(),
                            categories=categories.strip()
                        )
                    messages.success(request, "CSV data successfully imported.")
                    return HttpResponseRedirect("../")  # Redirect back to quote admin page
                except Exception as e:
                    messages.error(request, f"Error reading CSV: {e}")
        else:
            form = CSVUploadForm()

        return render(
            request,
            "admin/upload_csv.html",  # Custom template for CSV upload
            {"form": form}
        )

# Register the Quote model with the custom admin
admin.site.register(PreQuote, QuoteAdmin)
