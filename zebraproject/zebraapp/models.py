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
    detail = models.TextField(null=True)
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
    likes = models.IntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.name)

class MyItem(models.Model):
    itemName = models.CharField(max_length=200)
    itemShop = models.CharField(max_length=200)
    itemDate = models.DateTimeField('date published')
    
    class Meta:
        ordering = ['-itemDate']

    def __str__(self):
        return self.itemDate.strftime("%Y.%m.%d") + "-" + self.itemName + "-" + self.itemShop

class Tip(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    cover = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title

class TipBody(models.Model):
    tip = models.ForeignKey(Tip, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    product = models.ForeignKey(ChildProduct, on_delete=models.CASCADE, related_name='product_likes')
    quantity = models.IntegerField(default=1)



