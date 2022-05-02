from django import forms
from django.forms import widgets, ModelForm, IntegerField
from .models import Ohc 
from crispy_forms.helper import FormHelper
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget


class OhcForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(OhcForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['eval_1'].required = False
        self.fields['eval_2'].required = False
        self.fields['eval_3'].required = False
        self.fields['eval_4'].required = False
        self.fields['eval_5'].required = False
        self.fields['eval_6'].required = False
        self.fields['eval_7'].required = False
        self.fields['eval_8'].required = False
        self.fields['eval_9'].required = False

    class Meta:
        model = Ohc
        fields = '__all__'
        labels = {
            'candidate_Initial': '',
            'candidate_Signature': '',
            'candidate_Checkbox': '',
            'candidateTopsId': 'Tops ID',
            'candidate_DOB': 'Date of Birth',
            'candidate_NIN': 'National Insurance No.',
            'machine_Make_Model': 'Make/Model',
            'machine_Motive_Power': 'Motive Power',
            'machine_Capacity': 'Capacity in Kgs',
            'machine_Load_Centre': 'Load Centre in mm',
            'machine_Test_Lift_Height': 'Test lift height in mm',
            'testPass': 'Pass',
            'testFail': 'Fail (Over 40 penalty points)',
            'testDate': 'Test Date:',
            'courseTypeN': 'Novice',
            'courseTypeE': 'Experienced',
            'courseTypeC': 'Conversion',
            'courseTypeSF': 'Safety Refresher',
            'special_Application': 'Special Application (Please Specify)',
            'static_Travelling': 'Static/Travelling',
            'd1_JS': 'd1_js',
            'd2_JS': 'd2_js',
            'd3_JS': 'd3_js',
            'd4_JS': 'd4_js',
            'd5_JS': 'd5_js',
            'd1_SD': 'd1_sd',
            'd2_SD': 'd2_sd',
            'd3_SD': 'd3_sd',
            'd4_SD': 'd4_sd',
            'd5_SD': 'd5_sd',
            'd1_LC': 'd1_lc',
            'd2_LC': 'd2_lc',
            'd3_LC': 'd3_lc',
            'd4_LC': 'd4_lc',
            'd5_LC': 'd5_lc',
            'd1_M': 'd1_m',
            'd2_M': 'd2_m',
            'd3_M': 'd3_m',
            'd4_M': 'd4_m',
            'd5_M': 'd5_m',
            'd1_SA': 'd1_sa',
            'd2_SA': 'd2_sa',
            'd3_SA': 'd3_sa',
            'd4_SA': 'd4_sa',
            'd5_SA': 'd5_sa',
            'instructor_Comments': '',
            'instructor_2': '',
            'penalty_1': 'penalty_1',
            'penalty_2': 'penalty_2',
            'penalty_3': 'penalty_3',
            'penalty_4': 'penalty_4',
            'penalty_5': 'penalty_5',
            'penalty_6': 'penalty_6',
            'penalty_7': 'penalty_7',
            'penalty_8': 'penalty_8',
            'penalty_9': 'penalty_9',
            'penalty_10': 'penalty_10',
            'penalty_11': 'penalty_11',
            'penalty_12': 'penalty_12',
            'penalty_13': 'penalty_13',
            'penalty_14': 'penalty_14',
            'penalty_15': 'penalty_15',
            'penalty_16': 'penalty_16',
            'penalty_17': 'penalty_17',
            'penalty_18': 'penalty_18',
            'penalty_19': 'penalty_19',
            'penalty_20': 'penalty_20',
            'penalty_21': 'penalty_21',
            'penalty_22': 'penalty_22',
            'penalty_23': 'penalty_23',
            'penalty_24': 'penalty_24',
            'penalty_25': 'penalty_25',
            'penalty_26': 'penalty_26',
            'penalty_27': 'penalty_27',
            'penalty_28': 'penalty_28',
            'penalty_29': 'penalty_29',
            'md_1': 'md_1',
            'md_2': 'md_2',
            'md_3': 'md_3',
            'md_4': 'md_4',
            'md_5': 'md_5',
            'md_6': 'md_6',
            'md_7': 'md_7',
            'md_8': 'md_8',
            'sop': '*S.O.P',
            'cs': '**C.S',
            'mark_1': 'mark_1',
            'mark_2': 'mark_2',
            'mark_3': 'mark_3',
            'mark_4': 'mark_4',
            'mark_5': 'mark_5',
            'mark_6': 'mark_6',
            'mark_7': 'mark_7',
            'mark_8': 'mark_8',
            'mark_9': 'mark_9',
            'mark_10': 'mark_10',
            'mark_11': 'mark_11',
            'mark_12': 'mark_12',
            'mark_13': 'mark_13',
            'mark_14': 'mark_14',
            'mark_15': 'mark_15',
            'mark_16': 'mark_16',
            'mark_17': 'mark_17',
            'mark_18': 'mark_18',
            'mark_19': 'mark_19',
            'mark_20': 'mark_20',
            'mark_21': 'mark_21',
            'mark_22': 'mark_22',
            'mark_23': 'mark_23',
            'mark_24': 'mark_24',
            'mark_25': 'mark_25',
            'question_1': 'question_1',
            'question_2': 'question_2',
            'question_3': 'question_3',
            'question_4': 'question_4',
            'question_5': 'question_5',
            'question_6': 'question_6',
            'question_7': 'question_7',
            'question_8': 'question_8',
            'question_9': 'question_9',
            'question_10': 'question_10',
            'question_11': 'question_11',
            'question_12': 'question_12',
            'question_13': 'question_13',
            'question_14': 'question_14',
            'question_15': 'question_15',
            'question_16': 'question_16',
            'question_17': 'question_17',
            'question_18': 'question_18',
            'question_19': 'question_19',
            'question_20': 'question_20',
            'question_21': 'question_21',
            'question_22': 'question_22',
            'question_23': 'question_23',
            'question_24': 'question_24',
            'question_25': 'question_25',
            'e_testDate': 'Test Date',
            'course_Timing': 'Overall Timing Of Course',
            'preUseEM_1': 'preuseem_1',
            'preUseEM_2': 'preuseem_2',
            'preUseEM_3': 'preuseem_3',
            'preUseEM_4': 'preuseem_4',
            'preUseEM_5': 'preuseem_5',
            'preUseEM_6': 'preuseem_6',
            'preUseEM_7': 'preuseem_7',
            'preUseEM_8': 'preuseem_8',
            'preUseEM_9': 'preuseem_9',
            'preUseEM_10': 'preuseem_10',
            'preUseEM_11': 'preuseem_11',
            'preUseEM_12': 'preuseem_12',
            'preUseEM_13': 'preuseem_13',
            'preUseEM_14': 'preuseem_14',
            'preUseEM_15': 'preuseem_15',
            'preUseEM_16': 'preuseem_16',
            'preUseEM_17': 'preuseem_17',
            'preUseEM_18': 'preuseem_18',
            'preUseEM_CRP': 'Pass',
            'preUseEM_CRR': 'Refer',
            'preUseEM_CRTD': 'Re-Test Date',
            'instructor_2': ' ',
            'BO_attachments': 'Attachments',
            'BO_D1': 'bo_d1',
            'BO_D2': 'bo_d2',
            'BO_D3': 'bo_d3',
            'BO_D4': 'bo_d4',
            'BO_D5': 'bo_d5',
            'BO_D6': 'bo_d6',
            'BO_D7': 'bo_d7',
            'BO_D8': 'bo_d8',
            'BO_D9': 'bo_d9',
            'BO_D10': 'bo_d10',
            'BO_D11': 'bo_d11',
            'BO_D12': 'bo_d12',
            'BO_D13': 'bo_d13',
            'BO_D14': 'bo_d14',
            'BO_D15': 'bo_d15',
            'BO_D16': 'bo_d16',
            'BO_D17': 'bo_d17',
            'BO_D18': 'bo_d18',
            'BO_D19': 'bo_d19',
            'BO_D20': 'bo_d20',
            'BO_D21': 'bo_d21',
            'instructorAdditionalComments': 'Instructor Additional Comments',
            'eval_1': 'eval_1',
            'eval_2': 'eval_2',
            'eval_3': 'eval_3',
            'eval_4': 'eval_4',
            'eval_5': 'eval_5',
            'eval_6': 'eval_6',
            'eval_7': 'eval_7',
            'eval_8': 'eval_8',
            'eval_9': 'eval_9',
            'eval_10': '',
            'eval_11': '',
            'eval_12': '',
        }
        group = [('',''), ('2 Way', '2 Way'), ('4 Way', '4 Way')]
        motive_power = [('',''), ('Electric', 'Electric'), ('Diesel', 'Diesel'), ('Pedestrian', 'Pedestrian')]
        operator_choices = [('',''), ('A','A'), ('B','B'), ('C','C'), ('D','D'), ('E', 'E')]
        test_results = [('',''), ('Pass', 'Pass'), ('Referral', 'Referral')]
        check_choices = [('',''), ('N/A', 'N/A'), ('cc', 'Check Completed'), ('cr', 'Check Referred'),]
        question_choices = [('',''), ('A','A'), ('B','B'), ('C','C'), ('D','D')]
        mark_choices = [('0',''), ('0', '0'), ('4', '4')]
        mark_choices1 = [('0',''), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')]
        type = [('',''), ('Overhead Crane','Overhead Crane')]
        static_Travelling = [('',''), ('Static', 'Static'), ('Travelling', 'Travelling')]
        widgets = {
            'completed': widgets.CheckboxInput(attrs={'style':'width:30px;height:30px;', 'class': 'align-self-center'}),
            'audit_Completed': widgets.CheckboxInput(attrs={'style':'width:30px;height:30px;', 'class': 'align-self-center'}),
            'has_Certificate': widgets.CheckboxInput(attrs={'style':'width:30px;height:30px;', 'class': 'align-self-center'}),
            'audit_Notes': forms.Textarea(attrs={'rows':3, 'class': 'w-100'}),
            'candidate_Name': forms.TextInput(attrs = {'onchange' : "updateCandidateName();"}),
            'candidate_Initial': forms.TextInput(attrs = {'placeholder':'Initials' ,'onchange' : "initialAll();"}),
            'candidateTopsId': forms.TextInput(attrs = {'onchange' : "updateTopsID();"}),
            'course_Type': forms.TextInput(),
            'instructor': forms.Select(attrs={'onchange' : "instructorCall();"}),
            'instructor_2': forms.Select(attrs={'onchange' : "instructor2Call();"}),
            'company_Name': forms.Select(attrs={'onchange' : "get_customer();"}),
            'machine_Test_Lift_Height': forms.NumberInput(attrs={'onchange' : "liftHeightAutofill();", 'class': 'testHeight'}),
            'machine_Capacity': forms.NumberInput(attrs={'onchange' : "capacityAutofill();", 'class': 'capacity'}),
            'start_Date': widgets.DateInput(attrs={'type': 'date', 'onchange' : "startDateAutofill();"}),
            'finish_Date': widgets.DateInput(attrs={'type': 'date', 'onchange' : "endDateAutofill();"}),
            'penalty_1': widgets.NumberInput(attrs={'class': 'award carryForward'}),
            'penalty_2': widgets.NumberInput(attrs={'class': 'award carryForward'}),
            'penalty_3': widgets.NumberInput(attrs={'class': 'award carryForward'}),
            'penalty_4': widgets.NumberInput(attrs={'class': 'award carryForward'}),
            'penalty_5': widgets.NumberInput(attrs={'class': 'award carryForward'}),
            'penalty_6': widgets.NumberInput(attrs={'class': 'award carryForward'}),
            'penalty_7': widgets.NumberInput(attrs={'class': 'award carryForward'}),
            'penalty_8': widgets.NumberInput(attrs={'class': 'award carryForward'}),
            'penalty_9': widgets.NumberInput(attrs={'class': 'award carryForward'}),
            'penalty_10': widgets.NumberInput(attrs={'class': 'award carryForward'}),
            'penalty_11': widgets.NumberInput(attrs={'class': 'award carryForward'}),
            'penalty_12': widgets.NumberInput(attrs={'class': 'award carryForward'}),
            'penalty_13': widgets.NumberInput(attrs={'class': 'award carryForward'}),
            'penalty_14': widgets.NumberInput(attrs={'class': 'award carryForward'}),
            'penalty_15': widgets.NumberInput(attrs={'class': 'award carryForward'}),
            'penalty_16': widgets.NumberInput(attrs={'class': 'award carryForward'}),
            'penalty_17': widgets.NumberInput(attrs={'class': 'award carryForward'}),
            'penalty_18': widgets.NumberInput(attrs={'class': 'award carryForward'}),
            'penalty_19': widgets.NumberInput(attrs={'class': 'award carryForward'}),
            'penalty_20': widgets.NumberInput(attrs={'class': 'award'}),
            'penalty_21': widgets.NumberInput(attrs={'class': 'award'}),
            'penalty_22': widgets.NumberInput(attrs={'class': 'award'}),
            'penalty_23': widgets.NumberInput(attrs={'class': 'award'}),
            'penalty_24': widgets.NumberInput(attrs={'class': 'award'}),
            'penalty_25': widgets.NumberInput(attrs={'class': 'award'}),
            'penalty_26': widgets.NumberInput(attrs={'class': 'award'}),
            'penalty_27': widgets.NumberInput(attrs={'class': 'award'}),
            'penalty_28': widgets.NumberInput(attrs={'class': 'award'}),
            'penalty_29': widgets.NumberInput(attrs={'class': 'award'}),
            'penalty_30': widgets.NumberInput(attrs={'class': 'award'}),
            'penalty_31': widgets.NumberInput(attrs={'class': 'award'}),
            'penalty_32': widgets.NumberInput(attrs={'class': 'award'}),
            'penalty_33': widgets.NumberInput(attrs={'class': 'award'}),
            'penalty_34': widgets.NumberInput(attrs={'class': 'award'}),
            'penalty_35': widgets.NumberInput(attrs={'class': 'award'}),
            'penalty_36': widgets.NumberInput(attrs={'class': 'award'}),
            'penalty_37': widgets.NumberInput(attrs={'class': 'award'}),
            'venue': forms.Select(choices=(('',''), ('TTT','TTT'), ('On-Site','On-Site')), attrs = {'onchange' : "venueAutofill();"}),
            'candidate_Checkbox': widgets.CheckboxInput(attrs={'style':'width:40px;height:40px;float:none;'}),
            'candidate_DOB': widgets.DateInput(attrs={'type': 'date'}),
            'machine_Make_Model': forms.TextInput(attrs={'class':'truckModel', 'onchange': 'updateModel()'}),
            'machine_Group': forms.Select(choices=type, attrs={'class':'truckType', 'onchange': 'updateTruck()'}),
            'machine_Motive_Power': forms.Select(choices=motive_power, attrs={'class': 'motive', 'onchange': 'motiveAutofill()'}),
            'testPass': widgets.CheckboxInput(attrs={'style':'width:30px;height:30px;float:none;'}),
            'testFail': widgets.CheckboxInput(attrs={'style':'width:30px;height:30px;float:none;'}),
            'testDate': widgets.DateInput(attrs={'type': 'date'}),
            'courseTypeN': widgets.CheckboxInput(attrs={'style':'width:15px;height:15px;float:none;'}),
            'courseTypeE': widgets.CheckboxInput(attrs={'style':'width:15px;height:15px;float:none;'}),
            'courseTypeC': widgets.CheckboxInput(attrs={'style':'width:15px;height:15px;float:none;'}),
            'courseTypeSF': widgets.CheckboxInput(attrs={'style':'width:15px;height:15px;float:none;'}),
            'static_Travelling': forms.Select(choices=static_Travelling),
            'platform2': widgets.CheckboxInput(attrs={'style':'width:15px;height:15px;float:none;'}),
            'axles': widgets.CheckboxInput(attrs={'style':'width:15px;height:15px;float:none;'}),
            'stabilisers': widgets.CheckboxInput(attrs={'style':'width:15px;height:15px;float:none;'}),
            'basic_Skills': widgets.DateInput(attrs={'type':'date'}),
            'theory': widgets.DateInput(attrs={'type':'date'}),
            'pre_Shift': widgets.DateInput(attrs={'type':'date'}),
            'refresher_Test': widgets.DateInput(attrs={'type':'date'}),
            'familiarisation': widgets.DateInput(attrs={'type':'date'}),
            'specific_Job': widgets.DateInput(attrs={'type':'date'}),
            'd1_JS': forms.Select(choices=operator_choices),
            'd2_JS': forms.Select(choices=operator_choices),
            'd3_JS': forms.Select(choices=operator_choices),
            'd4_JS': forms.Select(choices=operator_choices),
            'd5_JS': forms.Select(choices=operator_choices),
            'd1_SD': forms.Select(choices=operator_choices),
            'd2_SD': forms.Select(choices=operator_choices),
            'd3_SD': forms.Select(choices=operator_choices),
            'd4_SD': forms.Select(choices=operator_choices),
            'd5_SD': forms.Select(choices=operator_choices),
            'd1_LC': forms.Select(choices=operator_choices),
            'd2_LC': forms.Select(choices=operator_choices),
            'd3_LC': forms.Select(choices=operator_choices),
            'd4_LC': forms.Select(choices=operator_choices),
            'd5_LC': forms.Select(choices=operator_choices),
            'd1_M': forms.Select(choices=operator_choices),
            'd2_M': forms.Select(choices=operator_choices),
            'd3_M': forms.Select(choices=operator_choices),
            'd4_M': forms.Select(choices=operator_choices),
            'd5_M': forms.Select(choices=operator_choices),
            'd1_SA': forms.Select(choices=operator_choices),
            'd2_SA': forms.Select(choices=operator_choices),
            'd3_SA': forms.Select(choices=operator_choices),
            'd4_SA': forms.Select(choices=operator_choices),
            'd5_SA': forms.Select(choices=operator_choices),
            'final_Grading': forms.Select(choices=operator_choices),
            'pre_Use_Test': forms.Select(choices=test_results),
            'overall_Result': forms.Select(choices=test_results),
            'start_Time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'finish_Time': forms.TimeInput(format='%H:%M', attrs={'type': 'time', 'onchange' : "calculateDuration();"}),
            'md_1': widgets.CheckboxInput(attrs={'style':'width:30px;height:30px;float:none;'}),
            'md_2': widgets.CheckboxInput(attrs={'style':'width:30px;height:30px;float:none;'}),
            'md_3': widgets.CheckboxInput(attrs={'style':'width:30px;height:30px;float:none;'}),
            'md_4': widgets.CheckboxInput(attrs={'style':'width:30px;height:30px;float:none;'}),
            'md_5': widgets.CheckboxInput(attrs={'style':'width:30px;height:30px;float:none;'}),
            'md_6': widgets.CheckboxInput(attrs={'style':'width:30px;height:30px;float:none;'}),
            'md_7': widgets.CheckboxInput(attrs={'style':'width:30px;height:30px;float:none;'}),
            'md_8': widgets.CheckboxInput(attrs={'style':'width:30px;height:30px;float:none;'}),
            'group': forms.Select(choices=group),
            'preUseEM_1': forms.Select(choices=check_choices),
            'preUseEM_2': forms.Select(choices=check_choices),
            'preUseEM_3': forms.Select(choices=check_choices),
            'preUseEM_4': forms.Select(choices=check_choices),
            'preUseEM_5': forms.Select(choices=check_choices),
            'preUseEM_6': forms.Select(choices=check_choices),
            'preUseEM_7': forms.Select(choices=check_choices),
            'preUseEM_8': forms.Select(choices=check_choices),
            'preUseEM_9': forms.Select(choices=check_choices),
            'preUseEM_10': forms.Select(choices=check_choices),
            'preUseEM_11': forms.Select(choices=check_choices),
            'preUseEM_12': forms.Select(choices=check_choices),
            'preUseEM_13': forms.Select(choices=check_choices),
            'preUseEM_14': forms.Select(choices=check_choices),
            'preUseEM_15': forms.Select(choices=check_choices),
            'preUseEM_16': forms.Select(choices=check_choices),
            'preUseEM_17': forms.Select(choices=check_choices),
            'preUseEM_18': forms.Select(choices=check_choices),
            'mark_1': forms.Select(choices=mark_choices, attrs={'class': 'atMark'}),
            'mark_2': forms.Select(choices=mark_choices, attrs={'class': 'atMark'}),
            'mark_3': forms.Select(choices=mark_choices, attrs={'class': 'atMark'}),
            'mark_4': forms.Select(choices=mark_choices, attrs={'class': 'atMark'}),
            'mark_5': forms.Select(choices=mark_choices, attrs={'class': 'atMark'}),
            'mark_6': forms.Select(choices=mark_choices, attrs={'class': 'atMark'}),
            'mark_7': forms.Select(choices=mark_choices, attrs={'class': 'atMark'}),
            'mark_8': forms.Select(choices=mark_choices, attrs={'class': 'atMark'}),
            'mark_9': forms.Select(choices=mark_choices, attrs={'class': 'atMark'}),
            'mark_10': forms.Select(choices=mark_choices, attrs={'class': 'atMark'}),
            'mark_11': forms.Select(choices=mark_choices, attrs={'class': 'atMark'}),
            'mark_12': forms.Select(choices=mark_choices, attrs={'class': 'atMark'}),
            'mark_13': forms.Select(choices=mark_choices, attrs={'class': 'atMark'}),
            'mark_14': forms.Select(choices=mark_choices, attrs={'class': 'atMark'}),
            'mark_15': forms.Select(choices=mark_choices, attrs={'class': 'atMark'}),
            'mark_16': forms.Select(choices=mark_choices, attrs={'class': 'atMark'}),
            'mark_17': forms.Select(choices=mark_choices, attrs={'class': 'atMark'}),
            'mark_18': forms.Select(choices=mark_choices, attrs={'class': 'atMark'}),
            'mark_19': forms.Select(choices=mark_choices, attrs={'class': 'atMark'}),
            'mark_20': forms.Select(choices=mark_choices, attrs={'class': 'atMark'}),
            'mark_21': forms.Select(choices=mark_choices1, attrs={'class': 'atMark'}),
            'mark_22': forms.Select(choices=mark_choices1, attrs={'class': 'atMark'}),
            'mark_23': forms.Select(choices=mark_choices1, attrs={'class': 'atMark'}),
            'mark_24': forms.Select(choices=mark_choices1, attrs={'class': 'atMark'}),
            'mark_25': forms.Select(choices=mark_choices1, attrs={'class': 'atMark'}),
            'question_1': forms.Select(choices=question_choices),
            'question_2': forms.Select(choices=question_choices),
            'question_3': forms.Select(choices=question_choices),
            'question_4': forms.Select(choices=question_choices),
            'question_5': forms.Select(choices=question_choices),
            'question_6': forms.Select(choices=question_choices),
            'question_7': forms.Select(choices=question_choices),
            'question_8': forms.Select(choices=question_choices),
            'question_9': forms.Select(choices=question_choices),
            'question_10': forms.Select(choices=question_choices),
            'question_11': forms.Select(choices=question_choices),
            'question_12': forms.Select(choices=question_choices),
            'question_13': forms.Select(choices=question_choices),
            'question_14': forms.Select(choices=question_choices),
            'question_15': forms.Select(choices=question_choices),
            'question_16': forms.Select(choices=question_choices),
            'question_17': forms.Select(choices=question_choices),
            'question_18': forms.Select(choices=question_choices),
            'question_19': forms.Select(choices=question_choices),
            'question_20': forms.Select(choices=question_choices),
            'question_21': forms.Textarea(attrs={'rows':3}),
            'question_22': forms.Textarea(attrs={'rows':3}),
            'question_23': forms.Textarea(attrs={'rows':3}),
            'question_24': forms.Textarea(attrs={'rows':3}),
            'question_25': forms.Textarea(attrs={'rows':3}),
            'e_testDate': widgets.DateInput(attrs={'type': 'date'}),
            'preUseEM_CRP': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'preUseEM_CRR': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'preUseEM_CRTD': widgets.DateInput(attrs={'type': 'date'}),
            'BO_D1': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D2': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D3': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D4': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D5': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D6': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D7': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D8': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D9': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D10': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D11': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D12': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D13': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D14': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D15': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D16': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D17': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D18': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D19': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D20': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D21': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D22': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D23': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'BO_D24': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
            'eval_1': forms.RadioSelect(attrs={'style':'width:25px;height:25px;float:none;'}),
            'eval_2': forms.RadioSelect(attrs={'style':'width:25px;height:25px;float:none;'}),
            'eval_3': forms.RadioSelect(attrs={'style':'width:25px;height:25px;float:none;'}),
            'eval_4': forms.RadioSelect(attrs={'style':'width:25px;height:25px;float:none;'}),
            'eval_5': forms.RadioSelect(attrs={'style':'width:25px;height:25px;float:none;'}),
            'eval_6': forms.RadioSelect(attrs={'style':'width:25px;height:25px;float:none;'}),
            'eval_7': forms.RadioSelect(attrs={'style':'width:25px;height:25px;float:none;'}),
            'eval_8': forms.RadioSelect(attrs={'style':'width:25px;height:25px;float:none;'}),
            'eval_9': forms.RadioSelect(attrs={'style':'width:25px;height:25px;float:none;'}),
            }