from django.urls import path
from . import views

urlpatterns = [
    path('pivotsteer/', views.PivotPage.as_view(), name="pivotsteer"),
    path('pivotsteer/<slug:pk>/', views.EditPivot.as_view(), name="edit_pivotsteer"), 
]