from django.contrib import admin
from django.urls import path
from authapp.views import index, customerDetail, CustomerCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    
    
    path('customer-detail/<int:item_id>/', customerDetail, name="customer-detail"),
    path('account/', CustomerCreateView.as_view(), name="account")
]