from django.contrib import admin
from .models import Category, Product , ChildProduct, MyItem
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ChildProduct)
admin.site.register(MyItem)