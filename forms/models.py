from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Forms(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    form_type = GenericForeignKey()
    completed = models.BooleanField(default=False)
    certificate = models.BooleanField(default=False)
    certificateNumber = models.CharField(max_length=20, null=True, blank=True)