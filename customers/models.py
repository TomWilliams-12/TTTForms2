from django.db import models


class Customers(models.Model):
    company_name = models.CharField(max_length=100, unique=True)
    company_address_line_1 = models.CharField(max_length=150, blank=True, null=True)
    company_address_line_2 = models.CharField(max_length=150, blank=True, null=True)
    company_address_line_3 = models.CharField(max_length=150, blank=True, null=True)
    company_address_line_4 = models.CharField(max_length=150, blank=True, null=True)
    company_address_city = models.CharField(max_length=150, blank=True, null=True)
    company_address_county = models.CharField(max_length=150, blank=True, null=True)
    company_address_post_code = models.CharField(max_length=150, blank=True, null=True)
    company_contact_first_name = models.CharField(max_length=50, blank=True, null=True)
    company_contact_last_name = models.CharField(max_length=50, blank=True, null=True)
    company_phone_number = models.IntegerField(blank=True, null=True)
    company_mobile_number = models.IntegerField(blank=True, null=True)
    company_fax_number = models.IntegerField(blank=True, null=True)
    company_ddi_number = models.CharField(max_length=50, blank=True, null=True)
    company_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.company_name