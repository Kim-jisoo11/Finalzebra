from django.contrib import admin
from .models import Category, Product , ChildProduct, MyItem, Tip, TipBody, Likes

class TipBodyInline(admin.TabularInline):
    model = TipBody

class TipAdmin(admin.ModelAdmin):
    inlines = [TipBodyInline, ]

class ChildProductInline(admin.TabularInline):
    model = ChildProduct

class ProductAdmin(admin.ModelAdmin):
    inlines = [ChildProductInline, ]

# Register your models here.

admin.site.register(Category)
admin.site.register(MyItem)
admin.site.register(Tip, TipAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Likes)
