from django.urls import path
from . import views

urlpatterns = [
    path('360/', views.ThreeSixtyPage.as_view(), name="360"),
    path('360/<slug:pk>/', views.EditThreeSixty.as_view(), name="edit_360"), 
]