from django import forms
from django.forms import widgets, ModelForm, IntegerField
from .models import Aw 
from crispy_forms.helper import FormHelper

class AwForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AwForm, self).__init__(*args, **kwargs)
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
        model = Aw
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
            'pMachineMakeModel': 'Petrol Cutter/Grinder',
            'pMachineGroup': 'Make/Model',
            'eMachineMakeModel': 'Hand Electric Grinder',
            'eMachineGroup': 'Make/Model',
            'bMachineMakeModel': 'Bench Grinder',
            'bMachineGroup': 'Make/Model',
            'sop': '*S.O.P',
            'mewpS': '** MEWP.S',
            'special_Application': 'Special Application (Please Specify)',
            'd1_JS': 'd1_js',
            'd1_SD': 'd1_sd',
            'd1_LC': 'd1_lc',
            'd1_M': 'd1_m',
            'd1_SA': 'd1_sa',
            'pre_Use_Test': '',
            'overall_Result': '',
            'instructor_Comments': '',
            'instructor_2': '',
            'test_1_t': 'test_1_t',
            'test_2_t': 'test_2_t',
            'test_3_t': 'test_3_t',
            'test_4_t': 'test_4_t',
            'test_5_t': 'test_5_t',
            'test_6_t': 'test_6_t',
            'test_7_t': 'test_7_t',
            'test_8_t': 'test_8_t',
            'test_9_t': 'test_9_t',
            'test_10_t': 'test_10_t',
            'test_11_t': 'test_11_t',
            'test_12_t': 'test_12_t',
            'test_13_t': 'test_13_t',
            'test_14_t': 'test_14_t',
            'test_15_t': 'test_15_t',
            'test_16_t': 'test_16_t',
            'test_17_t': 'test_17_t',
            'test_18_t': 'test_18_t',
            'test_19_t': 'test_19_t',
            'test_20_t': 'test_20_t',
            'test_21_t': 'test_21_t',
            'test_22_t': 'test_22_t',
            'test_23_t': 'test_23_t',
            'test_24_t': 'test_24_t',
            'test_25_t': 'test_25_t',
            'test_26_t': 'test_26_t',
            'test_27_t': 'test_27_t',
            'test_28_t': 'test_28_t',
            'test_29_t': 'test_29_t',
            'test_30_t': 'test_30_t',
            'test_31_t': 'test_31_t',
            'test_32_t': 'test_32_t',
            'test_33_t': 'test_33_t',
            'test_1_c': 'test_1_c',
            'test_2_c': 'test_2_c',
            'test_3_c': 'test_3_c',
            'test_4_c': 'test_4_c',
            'test_5_c': 'test_5_c',
            'test_6_c': 'test_6_c',
            'test_7_c': 'test_7_c',
            'test_8_c': 'test_8_c',
            'test_9_c': 'test_9_c',
            'test_10_c': 'test_10_c',
            'test_11_c': 'test_11_c',
            'test_12_c': 'test_12_c',
            'test_13_c': 'test_13_c',
            'test_14_c': 'test_14_c',
            'test_15_c': 'test_15_c',
            'test_16_c': 'test_16_c',
            'test_17_c': 'test_17_c',
            'test_18_c': 'test_18_c',
            'test_19_c': 'test_19_c',
            'test_20_c': 'test_20_c',
            'test_21_c': 'test_21_c',
            'test_22_c': 'test_22_c',
            'test_23_c': 'test_23_c',
            'test_24_c': 'test_24_c',
            'test_25_c': 'test_25_c',
            'test_26_c': 'test_26_c',
            'test_27_c': 'test_27_c',
            'test_28_c': 'test_28_c',
            'test_29_c': 'test_29_c',
            'test_30_c': 'test_30_c',
            'test_31_c': 'test_31_c',
            'test_32_c': 'test_32_c',
            'test_33_c': 'test_33_c',
            'md_1': 'md_1',
            'md_2': 'md_2',
            'md_3': 'md_3',
            'md_4': 'md_4',
            'md_5': 'md_5',
            'md_6': 'md_6',
            'md_7': 'md_7',
            'restriction_Detail': '',
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
            'preUseEM_CRP': 'Pass',
            'preUseEM_CRR': 'Refer',
            'preUseEM_CRTD': 'Re-Test Date',
            'instructor_2': ' ',
            'BO_Type1': 'Type',
            'BO_Type2': 'Type',
            'BO_Model1': 'Model',
            'BO_Model2': 'Model',
            'BO_Speed1': 'Speed',
            'BO_Speed2': 'Speed',
            'BO_Attachments1': 'Attachments',
            'BO_Attachments2': 'Attachments',
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
            'BO_D22': 'bo_d22',
            'BO_D23': 'bo_d23',
            'BO_D24': 'bo_d24',
            'BO_D25': 'bo_d25',
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
        
        operator_choices = [('',''), ('A','A'), ('B','B'), ('C','C'), ('D','D'), ('E', 'E')]
        test_results = [('',''), ('Pass', 'Pass'), ('Referral', 'Referral')]
        check_choices = [('',''), ('N/A', 'N/A'), ('cc', 'Check Completed'), ('cr', 'Check Referred'),]
        question_choices = [('',''), ('A','A'), ('B','B'), ('C','C'), ('D','D')]
        mark_choices = [('0',''), ('0', '0'), ('4', '4')]
        mark_choices1 = [('0',''), ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')]
        type = [('',''), ('Mobile Scissors','Mobile Scissors'), ('Static Scissors','Static Scissors'), ('Mobile VPP','Mobile VPP'), ('Static VPP','Static VPP'),]
        group1 = [('',''), ('2WD','2WD'), ('4WD', '4WD')]
        group2 = [('',''), ('2WS','2WS'), ('4WS', '4WS')]
        mobileStatic = [('',''), ('Mobile', 'Mobile'), ('Static', 'Static')]
        widgets = {
            'completed': widgets.CheckboxInput(attrs={'style':'width:30px;height:30px;', 'class': 'align-self-center'}),
            'audit_Completed': widgets.CheckboxInput(attrs={'style':'width:30px;height:30px;', 'class': 'align-self-center'}),
            'has_Certificate': widgets.CheckboxInput(attrs={'style':'width:30px;height:30px;', 'class': 'align-self-center'}),
            'audit_Notes': forms.Textarea(attrs={'rows':3, 'class': 'w-100'}),
            'candidate_Name': forms.TextInput(attrs = {'onchange' : "updateCandidateName();"}),
            'candidate_Initial': forms.TextInput(attrs = {'placeholder':'Initials' ,'onchange' : "initialAll();"}),
            'candidateTopsId': forms.TextInput(attrs = {'onchange' : "updateTopsID();"}),
            'instructor': forms.Select(attrs={'onchange' : "instructorCall();"}),
            'instructor_2': forms.Select(attrs={'onchange' : "instructor2Call();"}),
            'company_Name': forms.Select(attrs={'onchange' : "get_customer();"}),
            'pMachineMakeModel': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'eMachineMakeModel': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'bMachineMakeModel': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'start_Date': widgets.DateInput(attrs={'type': 'date', 'onchange' : "startDateAutofill();"}),
            'finish_Date': widgets.DateInput(attrs={'type': 'date', 'onchange' : "endDateAutofill();"}),
            'test_1_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_2_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_3_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_4_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_5_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_6_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_7_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_8_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_9_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_10_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_11_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_12_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_13_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_14_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_15_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_16_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_17_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_18_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_19_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_20_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_21_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_22_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_23_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_24_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_25_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_26_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_27_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_28_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_29_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_30_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_31_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_32_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'test_33_t': widgets.CheckboxInput(attrs={'style':'width:20px;height:20px;float:none;'}),
            'venue': forms.Select(choices=(('',''), ('TTT','TTT'), ('On-Site','On-Site')), attrs = {'onchange' : "venueAutofill();"}),
            'candidate_Checkbox': widgets.CheckboxInput(attrs={'style':'width:40px;height:40px;float:none;'}),
            'candidate_DOB': widgets.DateInput(attrs={'type': 'date'}),
            'machine_Make_Model': forms.TextInput(attrs={'class':'truckModel', 'onchange': 'updateModel()'}),
            'machine_Type': forms.Select(choices=type, attrs={'class':'truckType', 'onchange': 'updateTruck()'}),
            'testPass': widgets.CheckboxInput(attrs={'style':'width:30px;height:30px;float:none;'}),
            'testFail': widgets.CheckboxInput(attrs={'style':'width:30px;height:30px;float:none;'}),
            'testDate': widgets.DateInput(attrs={'type': 'date'}),
            'courseTypeN': widgets.CheckboxInput(attrs={'style':'width:15px;height:15px;float:none;'}),
            'courseTypeE': widgets.CheckboxInput(attrs={'style':'width:15px;height:15px;float:none;'}),
            'courseTypeC': widgets.CheckboxInput(attrs={'style':'width:15px;height:15px;float:none;'}),
            'courseTypeSF': widgets.CheckboxInput(attrs={'style':'width:15px;height:15px;float:none;'}),
            'group1': forms.Select(choices=group1),
            'group2': forms.Select(choices=group2),
            'mobileStatic': forms.Select(choices=mobileStatic),
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
            'd1_SD': forms.Select(choices=operator_choices),
            'd1_LC': forms.Select(choices=operator_choices),
            'd1_M': forms.Select(choices=operator_choices),
            'd1_SA': forms.Select(choices=operator_choices),
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
            'preUseEM_19': forms.Select(choices=check_choices),
            'preUseEM_20': forms.Select(choices=check_choices),
            'preUseEM_21': forms.Select(choices=check_choices),
            'preUseEM_22': forms.Select(choices=check_choices),
            'preUseEM_23': forms.Select(choices=check_choices),
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
            'BO_testDate': widgets.DateInput(attrs={'type': 'date'}),
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
            'BO_D25': widgets.DateInput(attrs={'type': 'date', 'class': 'sigDate', 'onchange' : "instructorSign();"}),
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