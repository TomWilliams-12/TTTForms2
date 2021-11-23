from django import forms
from django.forms import Form, widgets
from django.forms.fields import BooleanField, CharField, ChoiceField, DateField, IntegerField, TimeField
from datetime import datetime
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from crispy_forms.bootstrap import InlineRadios



class InductionForm(Form):
    def __init__(self, choices, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(InductionForm, self).__init__(*args, **kwargs)
        self.fields['course_type'].choices = choices
        self.fields['instructor'].initial = self.request.user.first_name
        for i in range(10):
            self.fields['initial_%d' % i] = CharField(label='', required=False,
             widget=widgets.DateInput(attrs={'placeholder': 'Initial'}))

    name = CharField(label='Candidate Name', max_length=100, required=True)
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
    def __init__(self, review_choices, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(ReviewForm, self).__init__(*args, **kwargs)
        for i in range(9):
            self.fields['review_%d' % (i + 1)] = ChoiceField(label='review_%d' % (i + 1), required=False, choices=review_choices,
                widget=forms.RadioSelect(attrs={'class': 'test'})
                )
        for i in range(3):
            self.fields['review_%d' % (i + 10)] = CharField(label='review_%d' % (i + 10), max_length=100, required=False, 
            widget= forms.TextInput
                           (attrs={'class':'w-100'}))
        self.helper = FormHelper()
        self.helper.form_show_labels = False


class PracticalForm(Form):
    def __init__(self, test, test2, md, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(PracticalForm, self).__init__(*args, **kwargs)
        for k, v in test.items():
            if v['t'] == False:
                self.fields['penalty_'+v['num']] = IntegerField(label='penalty_'+v['num'], required=False, widget=widgets.NumberInput(attrs={'style': 'width:5ch'}))
        for k, v in test2.items():
            if v['t'] == False:
                self.fields['penalty_'+v['num']] = IntegerField(label='penalty_'+v['num'], required=False, widget=widgets.NumberInput(attrs={'style': 'width:5ch'}))
        counter = 1
        for i in md:
            self.fields['md_'+ str(counter)] = BooleanField(label='md_'+ str(counter), required=False, widget=widgets.CheckboxInput(attrs={'style':'width:30px;height:30px;float:none;'}))
            counter += 1

    set_time = IntegerField(label="Set Time (in minutes)", required=False)
    start_time = TimeField(required=False, widget=widgets.TimeInput(attrs={'type': 'time'}))
    finish_time = TimeField(required=False, widget=widgets.TimeInput(attrs={'type': 'time'}))


class TheoryForm(Form):
    question_choices = [('',''), ('A','A'), ('B','B'), ('C','C'), ('D','D')]
    mark_choices = [('',''), ('0', '0'), ('4', '4')]
    mark_choices1 = [('',''), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')]
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(TheoryForm, self).__init__(*args, **kwargs)
        
        for i in range(25):
            if i < 20:
                self.fields['question_'+ str(i + 1)] = ChoiceField(label='question_'+ str(i + 1), choices=self.question_choices)
                self.fields['mark_'+ str(i+1)] = ChoiceField(label='mark_'+ str(i + 1), choices=self.mark_choices)
            elif i >= 20:
                self.fields['question_'+ str(i + 1)] = CharField(label='question_'+ str(i + 1), widget=forms.Textarea(attrs={'rows':3}))
                self.fields['mark_'+ str(i+1)] = ChoiceField(label='mark_'+ str(i + 1), choices=self.mark_choices1)

    test_reference = CharField(label='Test Paper Reference', required=False)
