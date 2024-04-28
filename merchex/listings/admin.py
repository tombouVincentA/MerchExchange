from django.contrib import admin

from listings.models import Band, Listing

class BandAdminDisplay(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste

class ListingAdminDisplay(admin.ModelAdmin):
    list_display = ('title', 'description', 'sold', 'year', 'type')

# Register your models here.
#Band
admin.site.register(Band, BandAdminDisplay)

# Listing
admin.site.register(Listing, ListingAdminDisplay)