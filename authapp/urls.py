from django.contrib import admin
from django.urls import path
from authapp.views import CustomerCreateView, LoginView, LogoutView, ChangePassword


urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', CustomerCreateView.as_view(), name="account"),
    path('', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('ChangePassword/', ChangePassword.as_view(), name='ChangePassword'),
]