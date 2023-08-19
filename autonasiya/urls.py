from django.contrib import admin
from django.urls import path, include
from authapp.views import CustomerCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authapp.urls')),
    path('account/', include('core.urls')),
]