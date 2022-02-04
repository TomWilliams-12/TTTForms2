from django.urls import path
from . import views


urlpatterns = [
    path('create-certificate/', views.CreateCertificate.as_view(), name="create-certificate"),
    path('certificates/', views.CertificateListView.as_view(), name="certificates"),
    path('certificates/<slug:pk>/', views.Certificate.as_view(), name="certificate"),
    path('certificates/<slug:pk>/pdf', views.PDFCertificate.as_view(), name="pdfcertificate"),
]
