from django.contrib import admin
from django.urls import path
from authapp.views import index, customerDetail, CustomerCreateView, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    # path('profile/', index, name="index"),
    path('customer-detail/<int:pk>/', customerDetail, name="customer-detail"),
    path('account/', CustomerCreateView.as_view(), name="account"),
    
]