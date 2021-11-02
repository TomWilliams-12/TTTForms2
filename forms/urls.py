from django.urls import path
from . import views


urlpatterns = [
    path('induction', views.InductionPage.as_view(), name="induction"),
    path('review', views.ReviewPage.as_view(), name="review"),
]
