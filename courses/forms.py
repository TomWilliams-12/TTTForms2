from django.forms import ModelForm, widgets
from courses.models import Courses

class CourseForm(ModelForm):

    class Meta:
        model = Courses
        fields = '__all__'
        exclude = ()
        widgets = {
            'start_date': widgets.DateInput(attrs={'type': 'date'}),
        }


