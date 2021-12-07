from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from courses.models import Courses
from forms.models import Forms
from accounts.models import Profile
from customers.models import Customers
from jsignature.fields import JSignatureField

class Cbr(models.Model):
    form = GenericRelation(Forms)
    candidateName = models.CharField(max_length=50)
    courseType = models.CharField(max_length=50, blank=True, null=True)
    courseNumber = models.ForeignKey(Courses, related_name='course', on_delete=models.SET_NULL, null=True)
    venue = models.CharField(max_length=30, blank=True, null=True)
    startDate = models.DateField(blank=True, null=True)
    finishDate = models.DateField(blank=True, null=True)
    instructor = models.ForeignKey(Profile, related_name='instructor', on_delete=models.SET_NULL, null=True)
    candidateInitial = models.CharField(max_length=5, blank=True, null=True)
    candidateCheckbox = models.BooleanField()
    candidateSignature = JSignatureField(blank=True, null=True)
    candidateDOB = models.DateField(blank=True, null=True)
    candidateTopsId = models.CharField(max_length=20, blank=True, null=True)
    candidateNIN = models.CharField(max_length=9, blank=True, null=True)
    machineType = models.CharField(max_length=30, blank=True, null=True)
    machineGroup = models.CharField(max_length=5, blank=True, null=True)
    machineMakeModel = models.CharField(max_length=50, blank=True, null=True)
    machineCapacity = models.CharField(max_length=10, blank=True, null=True)
    machineLoadCentre = models.IntegerField(blank=True, null=True)
    machineTestLiftHeight = models.CharField(max_length=10, blank=True, null=True)
    machineAttachments = models.CharField(max_length=20, blank=True, null=True)
    machineMotivePower = models.CharField(max_length=20, blank=True, null=True)
    companyName = models.ForeignKey(Customers, related_name='customer', on_delete=models.SET_NULL, null=True)
    courseTypeN = models.BooleanField()
    courseTypeE = models.BooleanField()
    courseTypeC = models.BooleanField()
    courseTypeSF = models.BooleanField()
    courseTrainingRatio = models.CharField(max_length=10, blank=True, null=True)
    courseDuration = models.FloatField(blank=True, null=True)
    basicSkills = models.DateField(blank=True, null=True)
    theory = models.DateField(blank=True, null=True)
    preUse = models.DateField(blank=True, null=True)
    refresherTest = models.DateField(blank=True, null=True)
    familiarisation = models.DateField(blank=True, null=True)
    specificJob = models.DateField(blank=True, null=True)
    finalGrading = models.CharField(max_length=1, blank=True, null=True)
    basicSkillsTest = models.CharField(max_length=10, blank=True, null=True)
    theoryTest = models.CharField(max_length=10, blank=True, null=True)
    preUseTest = models.CharField(max_length=10, blank=True, null=True)
    overallResult = models.CharField(max_length=10, blank=True, null=True)
    instructorComments = models.CharField(max_length=1000, blank=True, null=True)
    instructor2Name = models.ForeignKey(Profile, related_name='instructor2', on_delete=models.SET_NULL, null=True)
    setTime = models.IntegerField(blank=True, null=True)
    startTime = models.TimeField(blank=True, null=True)
    finishTime = models.TimeField(blank=True, null=True)
    restrictionDetail = models.CharField(max_length=500, blank=True, null=True)
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
    Cbr.add_to_class('penalty_' + str(i + 1), models.IntegerField( blank=True, null=True))

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

for i in range(12):
    if i < 9:
        Cbr.add_to_class('eval_' + str(i + 1), models.CharField(max_length=1, blank=True, null=True))
    else:
        Cbr.add_to_class('eval_' + str(i + 1), models.CharField(max_length=300, blank=True, null=True))