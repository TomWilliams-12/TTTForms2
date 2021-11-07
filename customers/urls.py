from django.urls import path
from . import views


urlpatterns = [
    path('customer', views.CreateCustomer.as_view(), name="customer"),
    path('customers', views.ViewCustomers.as_view(), name="customers"),
    path('customer/<slug:pk>/', views.EditCustomer.as_view(), name="edit_customer"), 
]
