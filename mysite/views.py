from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from mysite.models import Profile, Category, Product, Photo, Order, OrderItem
from cart.cart import Cart

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

@login_required(login_url="/accounts/login/")
def cart_add(request, id):
    product = Product.objects.get(id=id)
    user = User.objects.get(username=request.user.username)
    next = request.GET.get("next")
    cart = Cart(request)
    cart.add(product=product)
    messages.add_message(request, messages.SUCCESS, "{} 添加成功".format(product.name))
    if next is not None:
        return redirect(next)
    return redirect("/category/")

@login_required(login_url="/accounts/login/")
def cart(request):
    plist = list()
    for k, v in request.session["cart"].items():
        item = dict()
        item[k] = v
        plist.append(item)
    return render(request, "cart.html", locals())

@login_required(login_url="/accounts/login/")
def cart_remove(request):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product=product)
    return redirect("/cart/")

@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("/cart/")
