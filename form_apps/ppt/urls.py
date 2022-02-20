from django.urls import path
from . import views

urlpatterns = [
    path('ppt/', views.PptPage.as_view(), name="ppt"),
    path('ppt/<slug:pk>/', views.EditPpt.as_view(), name="edit_ppt"), 
]
