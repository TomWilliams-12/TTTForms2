from django.db import models


class Customers(models.Model):
    company_name = models.CharField(max_length=100, unique=True)
    company_address = models.CharField(max_length=150, blank=True, null=True)
    company_contact = models.CharField(max_length=50, blank=True, null=True)
    company_number = models.IntegerField(blank=True, null=True)