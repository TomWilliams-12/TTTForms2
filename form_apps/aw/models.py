from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from courses.models import Courses
from forms.models import Forms
from accounts.models import Profile
from customers.models import Customers
from jsignature.fields import JSignatureField

class Aw(models.Model):
    def __str__(self):
            return 'aw'

    def course_type(self):
        return 'Abrasive Wheels'

    completed = models.BooleanField(default=False)
    audit_Notes = models.CharField(max_length=500, blank=True, null=True)
    audit_Completed = models.BooleanField(default=False)
    has_Certificate = models.BooleanField(default=False)
    form = GenericRelation(Forms)
    candidateTopsId = models.CharField(max_length=30, blank=True, null=True)
    machine_Group = models.CharField(max_length=30, blank=True, null=True)
    courseTypeN = models.BooleanField(default=False)
    courseTypeE = models.BooleanField(default=False)
    courseTypeC = models.BooleanField(default=False)
    courseTypeSF = models.BooleanField(default=False)
    candidate_Name = models.CharField(max_length=50)
    course_Type = models.CharField(max_length=50, blank=True, null=True)
    course_Number = models.ForeignKey(Courses, related_name='awCourse', on_delete=models.CASCADE, null=True, blank=True)
    venue = models.CharField(max_length=30, blank=True, null=True)
    start_Date = models.DateField(blank=True, null=True)
    finish_Date = models.DateField(blank=True, null=True)
    instructor = models.ForeignKey(Profile, related_name='awInstructor', on_delete=models.SET_NULL, null=True, blank=True)
    candidate_Initial = models.CharField(max_length=5, blank=True, null=True)
    candidate_Checkbox = models.BooleanField()
    signature = JSignatureField(blank=True, null=True)
    pMachineMakeModel = models.BooleanField()
    pMachineGroup = models.CharField(max_length=20, blank=True, null=True)
    eMachineMakeModel = models.BooleanField()
    eMachineGroup = models.CharField(max_length=20, blank=True, null=True)
    bMachineMakeModel = models.BooleanField()
    bMachineGroup = models.CharField(max_length=20, blank=True, null=True)
    set_Time = models.IntegerField(blank=True, null=True)
    start_Time = models.TimeField(blank=True, null=True)
    finish_Time = models.TimeField(blank=True, null=True)
    testPass = models.BooleanField()
    testFail = models.BooleanField()
    testDate = models.DateField(blank=True, null=True)
    candidate_DOB = models.DateField(blank=True, null=True)
    company_Name = models.ForeignKey(Customers, related_name='awCustomer', on_delete=models.SET_NULL, null=True, blank=True)
    course_Title = models.CharField(max_length=50, blank=True, null=True)
    course_Duration = models.CharField(max_length=20, blank=True, null=True)
    handheld = models.CharField(max_length=50, blank=True, null=True)
    petrol_Driven = models.CharField(max_length=50, blank=True, null=True)
    bench_Mounted = models.CharField(max_length=50, blank=True, null=True)
    other = models.CharField(max_length=50, blank=True, null=True)
    basic_Skills = models.DateField(blank=True, null=True)
    specific_Job = models.DateField(blank=True, null=True)
    refresher_Test = models.DateField(blank=True, null=True)
    familiarisation = models.DateField(blank=True, null=True)
    theory = models.DateField(blank=True, null=True)
    pre_Shift = models.DateField(blank=True, null=True)
    pre_Use_Test = models.CharField(max_length=5, blank=True, null=True)
    d1_JS = models.CharField(max_length=1, blank=True, null=True)
    d1_SD = models.CharField(max_length=1, blank=True, null=True)
    d1_LC = models.CharField(max_length=1, blank=True, null=True)
    d1_M = models.CharField(max_length=1, blank=True, null=True)
    d1_SA = models.CharField(max_length=1, blank=True, null=True)
    final_Grading = models.CharField(max_length=1, blank=True, null=True)
    instructor_Comments = models.CharField(max_length=1000, blank=True, null=True)
    theory_Test_Date = models.DateField(blank=True, null=True)
    theory_Paper_Number = models.CharField(max_length=10, blank=True, null=True)
    e_truckType = models.CharField(max_length=30, blank=True, null=True)
    e_model = models.CharField(max_length=30, blank=True, null=True)
    preUseEM_CRP = models.BooleanField()
    preUseEM_CRR = models.BooleanField()
    preUseEM_CRTD = models.DateField(blank=True, null=True)
    BO_testDate = models.DateField(blank=True, null=True)
    instructor_2 = models.ForeignKey(Profile, related_name='awInstructor2', on_delete=models.SET_NULL, null=True)
    BO_Type1 = models.CharField(max_length=30, blank=True, null=True)
    BO_Model1 = models.CharField(max_length=30, blank=True, null=True)
    BO_Speed1 = models.CharField(max_length=30, blank=True, null=True)
    BO_Attachments1 = models.CharField(max_length=30, blank=True, null=True)
    BO_Type2 = models.CharField(max_length=30, blank=True, null=True)
    BO_Model2 = models.CharField(max_length=30, blank=True, null=True)
    BO_Speed2 = models.CharField(max_length=30, blank=True, null=True)
    BO_Attachments2 = models.CharField(max_length=30, blank=True, null=True)
    training_Ratio = models.CharField(max_length=30, blank=True, null=True)
    course_Timing = models.CharField(max_length=30, blank=True, null=True)

for i in range(33):
    Aw.add_to_class('test_' + str(i + 1) + '_t', models.BooleanField())
    Aw.add_to_class('test_' + str(i + 1) + '_c', models.CharField(max_length=50, blank=True, null=True))
for i in range(6):
    Aw.add_to_class('md_' + str(i + 1), models.BooleanField())
for i in range(25):
    Aw.add_to_class('mark_' + str(i + 1), models.CharField(max_length=3, blank=True, null=True))
    if i + 1 < 21:
        Aw.add_to_class('question_' + str(i + 1), models.CharField(max_length=3, blank=True, null=True))
    else:
        Aw.add_to_class('question_' + str(i + 1), models.CharField(max_length=300, blank=True, null=True))
for i in range(27):
    Aw.add_to_class('preUseEM_' + str(i + 1), models.CharField(max_length=10, blank=True, null=True))
for i in range(25):
    Aw.add_to_class('BO_D' + str(i + 1), models.DateField(blank=True, null=True))
review_choices = [
        ('review_1','1'),
        ('review_2','2'),
        ('review_3','3'),
        ('review_4','4'),
        ('review_5','5'),
    ]
for i in range(12):
    if i < 9:
        Aw.add_to_class('eval_' + str(i + 1), models.CharField(choices=review_choices, max_length=10, blank=False, null=True, default=0))
    else:
        Aw.add_to_class('eval_' + str(i + 1), models.CharField(max_length=300, blank=True, null=True))