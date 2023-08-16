from django.contrib import admin
from django.urls import path
from authapp.views import index, detail, CustomerCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('detail/', detail, name="detail"),
    path('account/', CustomerCreateView.as_view(), name="account")
]