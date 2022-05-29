from django.urls import path
from . import views

urlpatterns = [
    path('boom/', views.BoomPage.as_view(), name="boom"),
    path('boom/<slug:pk>/', views.EditBoom.as_view(), name="edit_boom"), 
]