from django.contrib import admin
from .models import product,order, Location
import json
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'hybrid'})},
    }
# Register your models here.
@admin.register(product)
class ProductAdmin(admin.ModelAdmin):
	list_display=['name', 'Quality', 'category', 'quantity', 'price_ugx', 'price_drc']
	list_editable = ('quantity', )

@admin.register(order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ['Distributor', 'product', 'date', 'quantity', 'delivery_address', 'Telephone']

