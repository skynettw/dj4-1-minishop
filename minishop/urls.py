from django.contrib import admin
from django.urls import path, include
from mysite import views
from minishop import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('category/', views.category),
    path('category/<int:id>/', views.category),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
] 

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
admin.site.site_title = "迷你電商"
admin.site.site_header = "歡迎使用迷你電商"
admin.site.index_title = "迷你電商"
