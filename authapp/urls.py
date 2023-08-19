from django.contrib import admin
from django.urls import path
from authapp.views import CustomerCreateView, LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomerCreateView.as_view(), name="account"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
]