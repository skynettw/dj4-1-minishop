from django.shortcuts import render
from mysite.models import Profile, Category, Product, Photo, Order, OrderItem

def index(request):
    products = Product.objects.all().order_by('category')
    categories = Category.objects.all()
    return render(request, "index.html", locals())

def category(request, id=0):
    categories = Category.objects.all()
    if id == 0:
        cate_name = "所有商品"
        products = Product.objects.all().order_by('category')
    else:
        cate = Category.objects.get(id=id)
        cate_name = cate.name
        products = Product.objects.filter(category=cate)
    return render(request, "category.html", locals())
