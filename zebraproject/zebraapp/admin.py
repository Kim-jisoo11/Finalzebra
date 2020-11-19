from django.contrib import admin
from .models import Category, Product , ChildProduct 
# Register your models here.

class ChildProductInline(admin.TabularInline):
    model = ChildProduct

class ProductAdmin(admin.ModelAdmin):
    inlines = [ChildProductInline, ]

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)