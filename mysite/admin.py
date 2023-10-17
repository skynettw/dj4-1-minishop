from django.contrib import admin
from mysite.models import Profile, Category, Product, Photo, Order, OrderItem

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'phone']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['sku', 'category', 'name', 'image', 'description', 'price']

@admin.register(Photo)    
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['product', 'name', 'photo']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['no', 'user', 'order_date', 'status', 'memo']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'qty']
