# Create your views here.
from django.shortcuts import render
from .models import PreQuote
from django.core.paginator import Paginator
from django.db.models import Count
import random

def random_quotes_view(request):
    # Get all Quote IDs
    all_ids = list(PreQuote.objects.values_list('id', flat=True))
    random.shuffle(all_ids)  # Shuffle the list randomly

    # Fetch Quotes by the randomized IDs
    quotes = PreQuote.objects.filter(id__in=all_ids)

    # Preserve the order after shuffle (if order matters)
    quotes = sorted(quotes, key=lambda q: all_ids.index(q.id))

    # Paginate the quotes (50 per page)
    paginator = Paginator(quotes, 50)
    page_number = request.GET.get('page')  # Get current page number from URL
    page_obj = paginator.get_page(page_number)

    return render(request, 'userhome/quotes.html', {'page_obj': page_obj})
