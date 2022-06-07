from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from courses.models import Courses
from forms.models import Forms
from accounts.models import Profile
from customers.models import Customers
from jsignature.fields import JSignatureField

class Shovel(models.Model):
    def __str__(self):
        return 'loadingshovel'

    def course_type(self):
        return 'Loading Shovel'
    completed = models.BooleanField(default=False)
    audit_Notes = models.CharField(max_length=500, blank=True, null=True)
    audit_Completed = models.BooleanField(default=False)
    has_Certificate = models.BooleanField(default=False)
    form = GenericRelation(Forms)
    courseTypeN = models.BooleanField(default=False)
    courseTypeE = models.BooleanField(default=False)
    courseTypeC = models.BooleanField(default=False)
    courseTypeSF = models.BooleanField(default=False)
    candidateTopsId = models.CharField(max_length=30, blank=True, null=True)
    candidate_Name = models.CharField(max_length=50, blank=True, null=True)
    course_Type = models.CharField(max_length=50, blank=True, null=True)
    course_Number = models.ForeignKey(Courses, related_name='shovelCourse', on_delete=models.SET_NULL, null=True, blank=True)
    venue = models.CharField(max_length=30, blank=True, null=True)
    start_Date = models.DateField(blank=True, null=True)
    finish_Date = models.DateField(blank=True, null=True)
    instructor = models.ForeignKey(Profile, related_name='shovelInstructor', on_delete=models.SET_NULL, null=True, blank=True)
    candidate_Initial = models.CharField(max_length=5, blank=True, null=True)
    candidate_Checkbox = models.BooleanField()
    signature = JSignatureField(blank=True, null=True)
    machine_Group = models.CharField(max_length=50, blank=True, null=True)
    machine_Capacity = models.IntegerField(blank=True, null=True)
    bucket_Capacity = models.IntegerField(blank=True, null=True)
    motive_Traction = models.IntegerField(blank=True, null=True)
    attachments = models.CharField(max_length=50, blank=True, null=True)
    set_Time = models.IntegerField(blank=True, null=True)
    start_Time = models.TimeField(blank=True, null=True)
    finish_Time = models.TimeField(blank=True, null=True)
    test_Pass = models.BooleanField()
    test_Fail = models.BooleanField()
    test_Date = models.DateField(blank=True, null=True)
    candidate_DOB = models.DateField(blank=True, null=True)
    company_Name = models.ForeignKey(Customers, related_name='shovelCustomer', on_delete=models.SET_NULL, null=True, blank=True)
    course_Title = models.CharField(max_length=50, blank=True, null=True)
    course_Duration = models.CharField(max_length=20, blank=True, null=True)
    machine_Type = models.CharField(max_length=50, blank=True, null=True)
    machine_Model = models.CharField(max_length=50, blank=True, null=True)
    machine_Motive_Power = models.CharField(max_length=20, blank=True, null=True)
    rider_Pedestrian = models.CharField(max_length=15, blank=True, null=True)
    basic_Skills = models.DateField(blank=True, null=True)
    specific_Job = models.DateField(blank=True, null=True)
    refresher_Test = models.DateField(blank=True, null=True)
    familiarisation = models.DateField(blank=True, null=True)
    theory = models.DateField(blank=True, null=True)
    pre_Shift = models.DateField(blank=True, null=True)
    manoeuvring = models.CharField(max_length=5, blank=True, null=True)
    chicane = models.CharField(max_length=5, blank=True, null=True)
    low_Level = models.CharField(max_length=5, blank=True, null=True)
    eye_Level = models.CharField(max_length=5, blank=True, null=True)
    high_Level = models.CharField(max_length=5, blank=True, null=True)
    vert_Face = models.CharField(max_length=5, blank=True, null=True)
    sop = models.CharField(max_length=5, blank=True, null=True)
    fts = models.CharField(max_length=5, blank=True, null=True)
    vehicle_Loading = models.CharField(max_length=5, blank=True, null=True)
    ramps = models.CharField(max_length=5, blank=True, null=True)
    attachments_Initial = models.CharField(max_length=5, blank=True, null=True)
    special_Application = models.CharField(max_length=5, blank=True, null=True)
    pre_Use_Test = models.CharField(max_length=5, blank=True, null=True)
    final_Grading = models.CharField(max_length=1, blank=True, null=True)
    instructor_Comments = models.CharField(max_length=1000, blank=True, null=True)
    theory_Test_Date = models.DateField(blank=True, null=True)
    theory_Paper_Number = models.CharField(max_length=10, blank=True, null=True)
    e_testDate = models.DateField(blank=True, null=True)
    machine_Make = models.CharField(max_length=30, blank=True, null=True)
    e_abaCategory = models.CharField(max_length=30, blank=True, null=True)
    preUseEM_CRP = models.BooleanField()
    preUseEM_CRR = models.BooleanField()
    preUseEM_CRTD = models.DateField(blank=True, null=True)
    BO_testDate = models.DateField(blank=True, null=True)
    instructor_2 = models.ForeignKey(Profile, related_name='shovelInstructor2', on_delete=models.SET_NULL, null=True, blank=True)
    BO_truckType = models.CharField(max_length=30, blank=True, null=True)
    BO_truckModel = models.CharField(max_length=30, blank=True, null=True)
    BO_liftHeight = models.CharField(max_length=30, blank=True, null=True)
    BO_capacity = models.CharField(max_length=30, blank=True, null=True)
    BO_attachments = models.CharField(max_length=30, blank=True, null=True)
    training_Ratio = models.CharField(max_length=30, blank=True, null=True)
    course_Timing = models.CharField(max_length=30, blank=True, null=True)
    instructorAdditionalComments = models.CharField(max_length=3000, blank=True, null=True)

for i in range(7):
    Shovel.add_to_class('md_' + str(i + 1), models.BooleanField())
for i in range(37):
    Shovel.add_to_class('penalty_' + str(i + 1), models.IntegerField(blank=True, null=True))

for i in range(5):
    Shovel.add_to_class('d' + str(i + 1) + '_JS', models.CharField(max_length=1, blank=True, null=True))
    Shovel.add_to_class('d' + str(i + 1) + '_SD', models.CharField(max_length=1, blank=True, null=True))
    Shovel.add_to_class('d' + str(i + 1) + '_LC', models.CharField(max_length=1, blank=True, null=True))
    Shovel.add_to_class('d' + str(i + 1) + '_M', models.CharField(max_length=1, blank=True, null=True))
    Shovel.add_to_class('d' + str(i + 1) + '_SA', models.CharField(max_length=1, blank=True, null=True))

for i in range(25):
    Shovel.add_to_class('mark_' + str(i + 1), models.CharField(max_length=3, blank=True, null=True))
    if i + 1 < 21:
        Shovel.add_to_class('question_' + str(i + 1), models.CharField(max_length=3, blank=True, null=True))
    else:
        Shovel.add_to_class('question_' + str(i + 1), models.CharField(max_length=300, blank=True, null=True))

for i in range(22):
    Shovel.add_to_class('preUseEM_' + str(i + 1), models.CharField(max_length=10, blank=True, null=True))

for i in range(24):
    Shovel.add_to_class('BO_D' + str(i + 1), models.DateField(blank=True, null=True))

review_choices = [
    ('review_1','1'),
    ('review_2','2'),
    ('review_3','3'),
    ('review_4','4'),
    ('review_5','5'),
]
for i in range(12):
    if i < 9:
        Shovel.add_to_class('eval_' + str(i + 1), models.CharField(choices=review_choices, max_length=10, blank=False, null=True, default=0))
    else:
        Shovel.add_to_class('eval_' + str(i + 1), models.CharField(max_length=300, blank=True, null=True))