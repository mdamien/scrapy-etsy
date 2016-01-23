from django.contrib import admin

from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','shop','name','price','rating_count','views')
    list_display_links = ('name',)
    search_fields = ('name','shop','description')
    list_filter = ('available', 'price_currency')