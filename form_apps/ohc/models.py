from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from courses.models import Courses
from forms.models import Forms
from accounts.models import Profile
from customers.models import Customers
from jsignature.fields import JSignatureField

class Ohc(models.Model):
    def __str__(self):
        return 'ohc'

    def course_type(self):
        return 'Overhead Crane'

    completed = models.BooleanField(default=False)
    audit_Notes = models.CharField(max_length=500, blank=True, null=True)
    audit_Completed = models.BooleanField(default=False)
    has_Certificate = models.BooleanField(default=False)
    machine_Motive_Power = models.CharField(max_length=50, blank=True, null=True, default='Electric')
    machine_Type = models.CharField(max_length=50, blank=True, null=True, default='Overhead Crane')
    candidateTopsId = models.CharField(max_length=30, blank=True, null=True)
    courseTypeN = models.BooleanField(default=False)
    courseTypeE = models.BooleanField(default=False)
    courseTypeC = models.BooleanField(default=False)
    courseTypeSF = models.BooleanField(default=False)
    form = GenericRelation(Forms)
    candidate_Name = models.CharField(max_length=50)
    course_Type = models.CharField(max_length=50, blank=True, null=True)
    course_Number = models.ForeignKey(Courses, related_name='ohcCourse', on_delete=models.CASCADE, null=True, blank=True)
    venue = models.CharField(max_length=30, blank=True, null=True)
    start_Date = models.DateField(blank=True, null=True)
    finish_Date = models.DateField(blank=True, null=True)
    instructor = models.ForeignKey(Profile, related_name='ohcInstructor', on_delete=models.SET_NULL, null=True, blank=True)
    candidate_Initial = models.CharField(max_length=5, blank=True, null=True)
    candidate_Checkbox = models.BooleanField()
    signature = JSignatureField(blank=True, null=True)
    machine_Make_Model = models.CharField(max_length=50, blank=True, null=True)
    machine_Group = models.CharField(max_length=20, blank=True, null=True)
    machine_Capacity = models.IntegerField(blank=True, null=True)
    attachments = models.CharField(max_length=20, blank=True, null=True)
    static_Travelling = models.CharField(max_length=20, blank=True, null=True)
    set_Time = models.IntegerField(blank=True, null=True)
    start_Time = models.TimeField(blank=True, null=True)
    finish_Time = models.TimeField(blank=True, null=True)
    testPass = models.BooleanField()
    testFail = models.BooleanField()
    testDate = models.DateField(blank=True, null=True)
    candidate_DOB = models.DateField(blank=True, null=True)
    company_Name = models.ForeignKey(Customers, related_name='ohcCustomer', on_delete=models.SET_NULL, null=True, blank=True)
    course_Title = models.CharField(max_length=50, blank=True, null=True)
    course_Duration = models.CharField(max_length=20, blank=True, null=True)
    capacity = models.CharField(max_length=50, blank=True, null=True)
    group = models.CharField(max_length=5, blank=True, null=True)
    lifting_Accessories = models.CharField(max_length=50, blank=True, null=True)
    basic_Skills = models.DateField(blank=True, null=True)
    specific_Job = models.DateField(blank=True, null=True)
    refresher_Test = models.DateField(blank=True, null=True)
    familiarisation = models.DateField(blank=True, null=True)
    theory = models.DateField(blank=True, null=True)
    pre_Shift = models.DateField(blank=True, null=True)
    manoeuvring = models.CharField(max_length=5, blank=True, null=True)
    sop = models.CharField(max_length=5, blank=True, null=True)
    cs = models.CharField(max_length=5, blank=True, null=True)
    vehicle_Loading = models.CharField(max_length=5, blank=True, null=True)
    off_Loading = models.CharField(max_length=5, blank=True, null=True)
    attachments2 = models.CharField(max_length=5, blank=True, null=True)
    signalling_Communication = models.CharField(max_length=5, blank=True, null=True)
    special_Application = models.CharField(max_length=50, blank=True, null=True)
    pre_Use_Test = models.CharField(max_length=5, blank=True, null=True)
    final_Grading = models.CharField(max_length=1, blank=True, null=True)
    instructor_Comments = models.CharField(max_length=1000, blank=True, null=True)
    theory_Test_Date = models.DateField(blank=True, null=True)
    theory_Paper_Number = models.CharField(max_length=10, blank=True, null=True)
    e_testDate = models.DateField(blank=True, null=True)
    e_truckType = models.CharField(max_length=30, blank=True, null=True)
    e_model = models.CharField(max_length=30, blank=True, null=True)
    preUseEM_CRP = models.BooleanField()
    preUseEM_CRR = models.BooleanField()
    preUseEM_CRTD = models.DateField(blank=True, null=True)
    instructor_2 = models.ForeignKey(Profile, related_name='ohcInstructor2', on_delete=models.SET_NULL, null=True, blank=True)
    BO_attachments = models.CharField(max_length=30, blank=True, null=True)
    training_Ratio = models.CharField(max_length=30, blank=True, null=True)
    course_Timing = models.CharField(max_length=30, blank=True, null=True)
    instructorAdditionalComments = models.CharField(max_length=3000, blank=True, null=True)
for i in range(8):
    Ohc.add_to_class('md_' + str(i + 1), models.BooleanField())

for i in range(5):
    Ohc.add_to_class('d' + str(i + 1) + '_JS', models.CharField(max_length=1, blank=True, null=True))
    Ohc.add_to_class('d' + str(i + 1) + '_SD', models.CharField(max_length=1, blank=True, null=True))
    Ohc.add_to_class('d' + str(i + 1) + '_LC', models.CharField(max_length=1, blank=True, null=True))
    Ohc.add_to_class('d' + str(i + 1) + '_M', models.CharField(max_length=1, blank=True, null=True))
    Ohc.add_to_class('d' + str(i + 1) + '_SA', models.CharField(max_length=1, blank=True, null=True))

for i in range(25):
    Ohc.add_to_class('mark_' + str(i + 1), models.CharField(max_length=3, blank=True, null=True))
    if i + 1 < 21:
        Ohc.add_to_class('question_' + str(i + 1), models.CharField(max_length=3, blank=True, null=True))
    else:
        Ohc.add_to_class('question_' + str(i + 1), models.CharField(max_length=300, blank=True, null=True))

for i in range(29):
    Ohc.add_to_class('penalty_' + str(i + 1), models.IntegerField(blank=True, null=True))
for i in range(21):
    Ohc.add_to_class('BO_D' + str(i + 1), models.DateField(blank=True, null=True))
for i in range(18):
    Ohc.add_to_class('preUseEM_' + str(i + 1), models.CharField(max_length=10, blank=True, null=True))

review_choices = [
    ('review_1','1'),
    ('review_2','2'),
    ('review_3','3'),
    ('review_4','4'),
    ('review_5','5'),
]
for i in range(12):
    if i < 9:
        Ohc.add_to_class('eval_' + str(i + 1), models.CharField(choices=review_choices, max_length=10, blank=False, null=True, default=0))
    else:
        Ohc.add_to_class('eval_' + str(i + 1), models.CharField(max_length=300, blank=True, null=True))