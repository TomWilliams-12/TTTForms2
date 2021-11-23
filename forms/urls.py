from django.urls import path
from . import views


urlpatterns = [
    path('induction', views.InductionPage.as_view(), name="induction"),
    path('review', views.ReviewPage.as_view(), name="review"),
    path('practical', views.PracticalPage.as_view(), name="practical"),
    path('theory', views.TheoryPage.as_view(), name="theory"),
]
