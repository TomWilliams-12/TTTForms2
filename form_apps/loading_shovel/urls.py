from django.urls import path
from . import views

urlpatterns = [
    path('loadingshovel/', views.ShovelPage.as_view(), name="loadingshovel"),
    path('loadingshovel/<slug:pk>/', views.EditShovel.as_view(), name="edit_loadingshovel"), 
]