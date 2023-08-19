from django.contrib import admin
from django.urls import path
from authapp.views import index, customerDetail, CustomerCreateView
from core.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('login/', login_view, name="login"),
    path('customer-detail/<int:pk>/', customerDetail, name="customer-detail"),
    path('account/', CustomerCreateView.as_view(), name="account"),
    
]