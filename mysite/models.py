from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(default="")
    def __str__(self):
        return self.name

class Product(models.Model):
    sku = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.TextField(default="")
    price = models.IntegerField()
    image = models.ImageField(upload_to="minishop", blank=True, null=True)
    def __str__(self):
        return self.name
    
class Photo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="minishop")
    def __str__(self):
        return self.name
    
ORDER_STATUS = [
    (0, "未付款"), 
    (1, "已付款，處理中"),
    (2, "已寄送"), 
    (3, "訂單完成")
]
class Order(models.Model):
    no = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0, choices=ORDER_STATUS)
    memo = models.TextField(default="")
    def __str__(self):
        return self.no

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    def __str__(self):
        return str(self.order, self.product)