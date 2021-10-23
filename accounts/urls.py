from django.urls import path
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register),
    url(r'^login/$', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('edit_user/', views.edit_user, name='edit_user'),
    ]