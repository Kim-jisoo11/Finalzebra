from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Category(models.Model):
    sort = models.CharField(max_length=255)

    def __str__(self):
        return '{}'.format(self.sort)


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    image = models.ImageField(upload_to='images/')
    detail = models.CharField(max_length = 255)
    pub_date = models.DateTimeField(auto_now_add = True, null=True)

    def __str__(self):
        return '{}'.format(self.name)


class ChildProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null =True)
    name = models.CharField(max_length=200,null=True)
    price = models.IntegerField()
    shopName = models.CharField(max_length=200, null=True)
    shopLink = models.TextField(null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    ship = models.CharField(max_length = 255 , null = True)

    def __str__(self):
        return '{}'.format(self.name)




