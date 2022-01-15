from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from courses.models import Courses
from forms.models import Forms
from accounts.models import Profile
from customers.models import Customers
from jsignature.fields import JSignatureField

class Cbr(models.Model):
    def __str__(self):
            return 'CB/R'

    form = GenericRelation(Forms)
    candidate_Name = models.CharField(max_length=50)
    course_Type = models.CharField(max_length=50, blank=True, null=True)
    course_Number = models.ForeignKey(Courses, related_name='course', on_delete=models.SET_NULL, null=True, blank=True)
    venue = models.CharField(max_length=30, blank=True, null=True)
    start_Date = models.DateField(blank=True, null=True)
    finish_Date = models.DateField(blank=True, null=True)
    instructor = models.ForeignKey(Profile, related_name='instructor', on_delete=models.SET_NULL, null=True, blank=True)
    candidate_Initial = models.CharField(max_length=5, blank=True, null=True)
    candidate_Checkbox = models.BooleanField()
    signature = JSignatureField(blank=True, null=True)
    candidate_DOB = models.DateField(blank=True, null=True)
    candidateTopsId = models.CharField(max_length=20, blank=True, null=True)
    candidate_NIN = models.CharField(max_length=9, blank=True, null=True)
    machine_Type = models.CharField(max_length=30, blank=True, null=True)
    machine_Group = models.CharField(max_length=5, blank=True, null=True)
    machine_Make_Model = models.CharField(max_length=50, blank=True, null=True)
    machine_Capacity = models.IntegerField(blank=True, null=True)
    machine_Load_Centre = models.IntegerField(blank=True, null=True)
    machine_Test_Lift_Height = models.IntegerField(blank=True, null=True)
    machine_Attachments = models.CharField(max_length=20, blank=True, null=True)
    machine_Motive_Power = models.CharField(max_length=20, blank=True, null=True)
    company_Name = models.ForeignKey(Customers, related_name='customer', on_delete=models.SET_NULL, null=True, blank=True)
    courseTypeN = models.BooleanField()
    courseTypeE = models.BooleanField()
    courseTypeC = models.BooleanField()
    courseTypeSF = models.BooleanField()
    training_Ratio = models.CharField(max_length=10, blank=True, null=True)
    course_Duration = models.FloatField(blank=True, null=True)
    basic_Skills = models.DateField(blank=True, null=True)
    theory = models.DateField(blank=True, null=True)
    pre_Use = models.DateField(blank=True, null=True)
    refresher_Test = models.DateField(blank=True, null=True)
    familiarisation = models.DateField(blank=True, null=True)
    specific_Job = models.DateField(blank=True, null=True)
    final_Grading = models.CharField(max_length=1, blank=True, null=True)
    pre_Use_Test = models.CharField(max_length=10, blank=True, null=True)
    overall_Result = models.CharField(max_length=10, blank=True, null=True)
    instructor_Comments = models.CharField(max_length=1000, blank=True, null=True)
    instructor_2 = models.ForeignKey(Profile, related_name='instructor2', on_delete=models.SET_NULL, null=True, blank=True)
    set_Time = models.IntegerField(blank=True, null=True)
    start_Time = models.TimeField(blank=True, null=True)
    finish_Time = models.TimeField(blank=True, null=True)
    restriction_Detail = models.CharField(max_length=500, blank=True, null=True)
    testPaperReference = models.CharField(max_length=10, blank=True, null=True)
    ot_12_L = models.BooleanField()
    ot_12_M = models.BooleanField()
    ot_12_H = models.BooleanField()
    ot_13_L = models.BooleanField()
    ot_13_M = models.BooleanField()
    ot_13_H = models.BooleanField()
    ot_14_L = models.BooleanField()
    ot_14_M = models.BooleanField()
    ot_14_H = models.BooleanField()
    ot_17_T = models.BooleanField()
    ot_17_P = models.BooleanField()
    ot_18_T = models.BooleanField()
    ot_18_P = models.BooleanField()
    ot_19_PU = models.BooleanField()
    ot_19_T = models.BooleanField()
    ot_19_P = models.BooleanField()

for i in range(37):
    Cbr.add_to_class('penalty_' + str(i + 1), models.IntegerField(blank=True, null=True))

for i in range(7):
    Cbr.add_to_class('md_' + str(i + 1), models.BooleanField())

for i in range(23):
    Cbr.add_to_class('check_' + str(i + 1) + '_cc', models.CharField(max_length=5, blank=True, null=True))
    Cbr.add_to_class('check_' + str(i + 1) + '_cr', models.BooleanField())

for i in range(5):
    Cbr.add_to_class('d' + str(i + 1) + '_SD', models.CharField(max_length=1, blank=True, null=True))
    Cbr.add_to_class('d' + str(i + 1) + '_RTI', models.CharField(max_length=1, blank=True, null=True))
    Cbr.add_to_class('d' + str(i + 1) + '_M', models.CharField(max_length=1, blank=True, null=True))
    Cbr.add_to_class('d' + str(i + 1) + '_SA', models.CharField(max_length=1, blank=True, null=True))

for i in range(25):
    Cbr.add_to_class('mark_' + str(i + 1), models.CharField(max_length=3, blank=True, null=True))
    if i + 1 < 21:
        Cbr.add_to_class('question_' + str(i + 1), models.CharField(max_length=3, blank=True, null=True))
    else:
        Cbr.add_to_class('question_' + str(i + 1), models.CharField(max_length=300, blank=True, null=True))

for i in range(19):
    Cbr.add_to_class('ot_' + str(i + 1), models.CharField(max_length=10, blank=True, null=True))
review_choices = [
        ('review_1','1'),
        ('review_2','2'),
        ('review_3','3'),
        ('review_4','4'),
        ('review_5','5'),
    ]
for i in range(12):
    if i < 9:
        Cbr.add_to_class('eval_' + str(i + 1), models.CharField(choices=review_choices, max_length=10, blank=False, null=True, default=0))
    else:
        Cbr.add_to_class('eval_' + str(i + 1), models.CharField(max_length=300, blank=True, null=True))