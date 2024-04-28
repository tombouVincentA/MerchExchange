from django.http import HttpResponse
from django.shortcuts import render

#Add
from listings.models import Band, Listing


def about(request):
    return render(request, 'listings/about.html')

def contact(request):
    return render(request, 'listings/contact.html')

def hello(request):
    # Get bands from data base
    bands = Band.objects.all()

    return render(request, 'bands/hello.html', {'bands': bands})

def listings(request):
    # Get listings from data base
    listings = Listing.objects.all()
    
    return render(request, 'listings/hello.html', {'listings':listings})