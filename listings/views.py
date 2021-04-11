from django.shortcuts import render

from .models import listing

def index(request):
    listings = listing.objects.all()

    context = {
        'listings':listings
    }

    return render(request,'listings/listings.html', context)

def get_listing(request):
    return render(request,'listings/listing.html')

def search(request):
    return render(request,'listings/search.html')