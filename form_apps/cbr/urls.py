from django.urls import path
from . import views

urlpatterns = [
    path('cbr/', views.CbrPage.as_view(), name="cbr"),
    path('cbr/<slug:pk>/', views.EditCbr.as_view(), name="edit_cbr"), 
]