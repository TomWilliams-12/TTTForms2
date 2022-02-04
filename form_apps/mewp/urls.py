from django.urls import path
from . import views

urlpatterns = [
    path('mewp/', views.MewpPage.as_view(), name="mewp"),
    path('mewp/<slug:pk>/', views.EditMewp.as_view(), name="edit_mewp"), 
]