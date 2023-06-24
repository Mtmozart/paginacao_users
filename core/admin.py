from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')



