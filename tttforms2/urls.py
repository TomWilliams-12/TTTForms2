from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('accounts.urls')),
    path('', include('courses.urls')),
    path('', include('forms.urls')),
    path('', include('form_apps.cbr.urls')),
    path('', include('customers.urls')),
]