from django.forms import Form, widgets
from django.forms.fields import BooleanField, CharField, ChoiceField, DateField
from datetime import datetime
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget


class InductionForm(Form):
    def __init__(self, choices, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(InductionForm, self).__init__(*args, **kwargs)
        self.fields['course_type'].choices = choices
        self.fields['instructor'].initial = self.request.user.first_name
        for i in range(10):
            self.fields['initial_%d' % i] = CharField(label='', required=False,
             widget=widgets.DateInput(attrs={'placeholder': 'Initial'}))

    name = CharField(label='Your Name', max_length=100, required=True)
    course_type = ChoiceField(label='Course Type', required=False)
    course_number = CharField(label='Course Number', required=False)
    instructor = CharField(label='Instructor', required=False)
    venue = ChoiceField(choices=(('',''), ('TTT','TTT'), ('On-Site','On-Site')), required=False, label='Venue')
    start_date = DateField(label='Start Date', required=False, widget=widgets.DateInput(attrs={'type': 'date'}), initial=datetime.today())
    finish_date = DateField(label='Finish Date', required=False, widget=widgets.DateInput(attrs={'type': 'date'}))
    topsid = CharField(label='Topsid', required=False, max_length=10)
    candidate_checkbox = BooleanField(label="", required=False, widget=widgets.CheckboxInput(attrs={'style':'width:40px;height:40px;float:none;'}))
    candidate_signature = JSignatureField(label="", required=False, widget=JSignatureWidget(jsignature_attrs={'color': '#000'}))

class ReviewForm(Form):
    test = CharField(label='test', max_length=100)