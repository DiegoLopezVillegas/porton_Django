import json
from django.contrib import admin
from django.db.models import Count
from .models import Product,Horse,Userdata,Sale,Cart
import requests

class HorseAdmin(admin.ModelAdmin):
    list_display = ('idHorse', 'breed', 'description', 'price', 'imagePath', 'bornOn')
    search_fields = ['breed']  # Agregar esta línea
    list_filter = ('breed',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(_count_horses=Count('idHorse'))
        return queryset
    
    def count_horses(self, horse):
        return horse._count_horses
    
    count_horses.admin_order_field = '_count_horses'
    count_horses.short_description = 'Count Horses'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('idProduct', 'nameProduct', 'description', 'price', 'imagePath', 'category', 'stock')
    search_fields = ['nameProduct', 'idProduct', 'category']  # Agregar esta línea
    list_filter = ('category',)

class UserdataAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'password', 'cellphone', 'address', 'dni', 'role', 'idCart')
    search_fields = ['dni', 'name', 'role']  # Agregar esta línea
    list_filter = ('role',)

class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'total', 'userEmail', 'dni', 'items', 'date')
    search_fields = ['id', 'date']  # Agregar esta línea
    list_filter = ()

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'items', 'total')
    search_fields = ['id']  # Agregar esta línea
    list_filter = ('id',)



# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Horse, HorseAdmin)
admin.site.register(Userdata, UserdataAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Cart, CartAdmin)


