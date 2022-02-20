from django.urls import path
from . import views

urlpatterns = [
    path('aw/', views.AwPage.as_view(), name="aw"),
    path('aw/<slug:pk>/', views.EditAw.as_view(), name="edit_aw"), 
]
