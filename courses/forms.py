from django.forms import ModelForm, DateField, widgets
from courses.models import Courses
from accounts.models import Profile

class CourseForm(ModelForm):

    class Meta:
        model = Courses
        fields = '__all__'
        exclude = ()
        widgets = {
            'start_date': widgets.DateInput(attrs={'type': 'date'}),
        }