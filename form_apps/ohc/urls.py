from django.urls import path
from . import views

urlpatterns = [
    path('ohc/', views.OhcPage.as_view(), name="ohc"),
    path('ohc/<slug:pk>/', views.EditOhc.as_view(), name="edit_ohc"), 
]