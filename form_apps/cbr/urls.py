from django.urls import path
from . import views


urlpatterns = [
    path('cbr/', views.CbrPage.as_view(), name="cbr"),
]
