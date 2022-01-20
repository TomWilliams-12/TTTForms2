from django.urls import path

from api import views

urlpatterns = [
    path('getinstructors/', views.getinstructors),
    path('getinstructor/<int:id>', views.getinstructor),
    path('getcustomers/', views.getcustomers),
    path('getcustomer/<int:id>', views.getcustomer),
]