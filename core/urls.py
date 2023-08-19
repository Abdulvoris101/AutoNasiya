from django.urls import path
from .views import productPurchaseDetail, index


urlpatterns = [
    path('product/<int:pk>/', productPurchaseDetail, name="product"),
    path('', index, name="index"),
]