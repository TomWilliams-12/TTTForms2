from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('accounts.urls')),
    path('', include('courses.urls')),
    path('', include('forms.urls')),
    path('', include('form_apps.cbr.urls')),
    path('', include('form_apps.mewp.urls')),
    path('', include('form_apps.ohc.urls')),
    path('', include('form_apps.aw.urls')),
    path('', include('form_apps.ppt.urls')),
    path('', include('form_apps.boom.urls')),
    path('', include('form_apps.pivot_steer.urls')),
    path('', include('customers.urls')),
    path('', include('api.urls')),
    path('', include('audit.urls')),
]
