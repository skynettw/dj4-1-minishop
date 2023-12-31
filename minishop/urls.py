from django.contrib import admin
from django.urls import path, include
from mysite import views
from minishop import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('order/', views.order, name="order"),
    path('order/detail/<int:id>/', views.order_detail),
    path('cart/', views.cart, name='cart'),
    path('cart/remove/<int:id>/', views.cart_remove, name="cart_remove"),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/increment/<int:id>/', views.cart_increment, name='increment'),
    path('cart/decrement/<int:id>/', views.cart_decrement, name='decrement'),
    path('cart/clear/', views.cart_clear, name='cart_clear'),
    path('category/', views.category),
    path('category/<int:id>/', views.category),
    path('admin/', admin.site.urls),
    path('profile/', views.profile),
    path('profile/edit/', views.profile_edit),
    path('accounts/profile/', views.profile),
    path('accounts/', include('registration.backends.default.urls')),
] 

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
admin.site.site_title = "迷你電商"
admin.site.site_header = "歡迎使用迷你電商"
admin.site.index_title = "迷你電商"
