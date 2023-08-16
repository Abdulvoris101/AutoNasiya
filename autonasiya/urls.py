from django.contrib import admin
from django.urls import path
from authapp.views import index, detail, CustomerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('detail/', detail, name="detail"),
    path('account/', CustomerView.as_view(), name="account")
]