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
def cart_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/cart/")

@login_required(login_url="/accounts/login/")
def cart_decrement(request, id):
    try:
        cart = Cart(request)
        product = Product.objects.get(id=id)
        cart.decrement(product=product)
    except:
        pass
    return redirect("/cart/")

@login_required(login_url="/accounts/login/")
def cart(request):
    total = 0
    for k, v in request.session["cart"].items():
        total += float(v["price"]) * float(v["quantity"])
    return render(request, "cart.html", locals())

@login_required(login_url="/accounts/login/")
def cart_remove(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product=product)
    return redirect("/cart/")

@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("/cart/")

@login_required(login_url="/accounts/login/")
def order(request):
    cart = Cart(request)
    total = 0
    try:
        user = User.objects.get(username=request.user.username)
        new_order = Order(user=user)
        new_order.save()
        for k, v in request.session["cart"].items():
            product = Product.objects.get(id=v["product_id"])
            qty = v['quantity']
            order_item = OrderItem(
                order = new_order,
                product = product,
                qty = qty
            )
            order_item.save()
            total += float(v["price"]) * float(v["quantity"])
        cart.clear()
        messages.add_message(request, messages.SUCCESS, "訂單成功")        
    except Exception as e:
        messages.add_message(request, messages.ERROR, "下訂失敗")
        print(e)
    return redirect("/cart/")

@login_required(login_url="/accounts/login/")
def profile(request):
    user = User.objects.get(username=request.user.username)
    try:
        profile = Profile.objects.get(user=user)
    except:
        profile = Profile(user=user, address="未填", phone="未填")
        profile.save()
    orders = Order.objects.filter(user=user)
    return render(request, "profile.html", locals())

@login_required(login_url="/accounts/login/")
def order_detail(request, id):
    user = User.objects.get(username=request.user.username)
    order = Order.objects.get(id=id)
    orderitems = OrderItem.objects.filter(order=order)
    return render(request, "order-detail.html", locals())