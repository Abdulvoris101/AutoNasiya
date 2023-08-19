from django.contrib import admin
from django.urls import path, include
from authapp.views import CustomerCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('authapp.urls')),
    path('', include('core.urls')),
]