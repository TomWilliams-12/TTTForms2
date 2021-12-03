from django import forms
from django.forms import Form, widgets, ModelMultipleChoiceField
from django.forms.fields import BooleanField, CharField, ChoiceField, DateField, IntegerField, TimeField
from datetime import datetime
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from crispy_forms.helper import FormHelper
from models import Customers, Cbr, Profile

class CbrForm(Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(CbrForm, self).__init__(*args, **kwargs)
        self.fields['companyName'].queryset = Customers.objects.all()
        self.fields['instructor2Name'].queryset = Profile.objects.all()

    type = [('',''), ('Counterbalance', 'Counterbalance'), ('Reach', 'Reach')]
    group = [('',''), ('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('B4', 'B4'),
            ('D1', 'D1'), ('D2', 'D2'), ('D3', 'D3'), ('G2', 'G2')]
    motive_power = [('',''), ('Electric', 'Electric'), ('Diesel', 'Diesel'), ('LPG', 'LPG')]
    course_duration = [('',''), ('5','5'), ('6','6'), ('7.5','7.5'), ('15','15'), ('22.5','22.5'), ('30','30'), ('37.5','37.5')]
    models = [('',''), ('Jungheinrich EFGDF16','Jungheinrich EFGDF16'), ('YALE ERP16 ATF','YALE ERP16 ATF'), 
            ('Jungheinrich ETM14','Jungheinrich ETM14'), ('CAT NR14K','CAT NR14K')]
    training_ratio = [('1-1-1', '1-1-1'), ('2-1-1', '2-1-1'), ('3-1-1', '3-1-1')]

    candidateDOB = DateField(label='Candidate DOB', required=False, widget=widgets.DateInput(attrs={'type': 'date'}))
    candidateTopsId = CharField(label='Tops ID', max_length=15, required=True)
    candidateNIN = CharField(label='National Insurance Number', max_length=10, required=False)
    machineType = ChoiceField(label='', choices=type, required=False)
    machineGroup = ChoiceField(label='', choices=group, required=False)
    machineMakeModel = CharField(label='', max_length=100, required=False)
    machineCapacity = CharField(label='', max_length=100, required=False)
    machineLoadCentre = IntegerField(label='', required=False)
    machineTestLiftHeight = CharField(label='', max_length=10, required=False)
    machineAttachments = CharField(label='', max_length=20, required=False)
    machineMotivePower = CharField(label='', max_length=10, required=False)
    companyName = ModelMultipleChoiceField(queryset=None, null=True)
    courseTypeN = BooleanField(label="", required=False, widget=widgets.CheckboxInput())
    courseTypeE = BooleanField(label="", required=False, widget=widgets.CheckboxInput())
    courseTypeC = BooleanField(label="", required=False, widget=widgets.CheckboxInput())
    courseTypeSF = BooleanField(label="", required=False, widget=widgets.CheckboxInput())
    courseTrainingRatio = ChoiceField(label='', max_length=10, required=False, choices=training_ratio)
    courseDuration = ChoiceField(label='', max_length=10, required=False, choices=course_duration)
    basicSkills =DateField(label='', required=False, widget=widgets.DateInput(attrs={'type': 'date'}))
    theory = DateField(label='', required=False, widget=widgets.DateInput(attrs={'type': 'date'}))
    preUse = DateField(label='', required=False, widget=widgets.DateInput(attrs={'type': 'date'}))
    refresherTest = DateField(label='', required=False, widget=widgets.DateInput(attrs={'type': 'date'}))
    familiarisation = DateField(label='', required=False, widget=widgets.DateInput(attrs={'type': 'date'}))
    specificJob = DateField(label='', required=False, widget=widgets.DateInput(attrs={'type': 'date'}))
    finalGrading = CharField(label='', max_length=10, required=False)
    basicSkillsTest = CharField(label='', max_length=10, required=False)
    theoryTest = CharField(label='', max_length=10, required=False)
    preUseTest = CharField(label='', max_length=10, required=False)
    overallResult = CharField(label='', max_length=10, required=False)
    instructorComments = CharField(label='', max_length=1000, required=False)
    instructor2Name = ModelMultipleChoiceField(queryset=None, null=True)

    restrictionDetail = CharField(label='', max_length=500, required=False)
    testPaperReference = CharField(label='', max_length=10, required=False)
    ot_12_L = BooleanField(label="", required=False, widget=widgets.CheckboxInput())
    ot_12_M = BooleanField(label="", required=False, widget=widgets.CheckboxInput())
    ot_12_H = BooleanField(label="", required=False, widget=widgets.CheckboxInput())
    ot_13_L = BooleanField(label="", required=False, widget=widgets.CheckboxInput())
    ot_13_M = BooleanField(label="", required=False, widget=widgets.CheckboxInput())
    ot_13_H = BooleanField(label="", required=False, widget=widgets.CheckboxInput())
    ot_14_L = BooleanField(label="", required=False, widget=widgets.CheckboxInput())
    ot_14_M = BooleanField(label="", required=False, widget=widgets.CheckboxInput())
    ot_14_H = BooleanField(label="", required=False, widget=widgets.CheckboxInput())
    ot_17_T = BooleanField(label="", required=False, widget=widgets.CheckboxInput())
    ot_17_P = BooleanField(label="", required=False, widget=widgets.CheckboxInput())
    ot_18_T = BooleanField(label="", required=False, widget=widgets.CheckboxInput())
    ot_18_P = BooleanField(label="", required=False, widget=widgets.CheckboxInput())
    ot_19_PU = BooleanField(label="", required=False, widget=widgets.CheckboxInput())
    ot_19_T = BooleanField(label="", required=False, widget=widgets.CheckboxInput())
    ot_19_P = BooleanField(label="", required=False, widget=widgets.CheckboxInput())