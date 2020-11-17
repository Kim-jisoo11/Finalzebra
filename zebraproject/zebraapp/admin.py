from django.contrib import admin
from .models import Category, Product , ChildProduct, MyItem, Tip, TipBody

class TipBodyInline(admin.TabularInline):
    model = TipBody

class TipAdmin(admin.ModelAdmin):
    inlines = [TipBodyInline, ]

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ChildProduct)
admin.site.register(MyItem)
admin.site.register(Tip, TipAdmin)
