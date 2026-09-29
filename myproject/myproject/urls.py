from django.contrib import admin
from django.urls import path, include  # Make sure to import 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),   # Routes all root traffic to your app
]