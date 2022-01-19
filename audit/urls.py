from django.urls import path
from . import views


urlpatterns = [
    path('audit', views.AuditView.as_view(), name="audit"),
]
