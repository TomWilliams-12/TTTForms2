from django.db import models
from django.db.models.deletion import SET_NULL

from accounts.models import Profile

class Courses(models.Model):
    course_number = models.CharField(max_length=15, unique=True)
    candidate_number = models.IntegerField(blank=True, null=True)
    course_type = models.CharField(max_length=30)
    start_date = models.DateField(blank=True, null=True)
    instructor = models.ForeignKey(Profile, related_name='courseInstructor', on_delete=SET_NULL, null=True)
    venue = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.course_number
