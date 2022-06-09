# Generated by Django 3.2.7 on 2022-06-05 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsignature.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0005_auto_20220410_1113'),
        ('courses', '0002_auto_20211024_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shovel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('audit_Notes', models.CharField(blank=True, max_length=500, null=True)),
                ('audit_Completed', models.BooleanField(default=False)),
                ('has_Certificate', models.BooleanField(default=False)),
                ('courseTypeN', models.BooleanField(default=False)),
                ('courseTypeE', models.BooleanField(default=False)),
                ('courseTypeC', models.BooleanField(default=False)),
                ('courseTypeSF', models.BooleanField(default=False)),
                ('candidateTopsId', models.CharField(blank=True, max_length=30, null=True)),
                ('candidate_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('course_Type', models.CharField(blank=True, max_length=50, null=True)),
                ('venue', models.CharField(blank=True, max_length=30, null=True)),
                ('start_Date', models.DateField(blank=True, null=True)),
                ('finish_Date', models.DateField(blank=True, null=True)),
                ('candidate_Initial', models.CharField(blank=True, max_length=5, null=True)),
                ('candidate_Checkbox', models.BooleanField()),
                ('signature', jsignature.fields.JSignatureField(blank=True, null=True)),
                ('machine_Group', models.CharField(blank=True, max_length=50, null=True)),
                ('machine_Capacity', models.IntegerField(blank=True, null=True)),
                ('bucket_Capacity', models.IntegerField(blank=True, null=True)),
                ('motive_Traction', models.IntegerField(blank=True, null=True)),
                ('attachments', models.CharField(blank=True, max_length=50, null=True)),
                ('platformY', models.BooleanField()),
                ('platformN', models.BooleanField()),
                ('set_Time', models.IntegerField(blank=True, null=True)),
                ('start_Time', models.TimeField(blank=True, null=True)),
                ('finish_Time', models.TimeField(blank=True, null=True)),
                ('test_Pass', models.BooleanField()),
                ('test_Fail', models.BooleanField()),
                ('test_Date', models.DateField(blank=True, null=True)),
                ('preUsePass', models.BooleanField()),
                ('preUseFail', models.BooleanField()),
                ('preUseDate', models.DateField(blank=True, null=True)),
                ('akPass', models.BooleanField()),
                ('akFail', models.BooleanField()),
                ('akDate', models.DateField(blank=True, null=True)),
                ('candidate_DOB', models.DateField(blank=True, null=True)),
                ('course_Title', models.CharField(blank=True, max_length=50, null=True)),
                ('course_Duration', models.CharField(blank=True, max_length=20, null=True)),
                ('machine_Type', models.CharField(blank=True, max_length=50, null=True)),
                ('machine_Model', models.CharField(blank=True, max_length=50, null=True)),
                ('machine_Motive_Power', models.CharField(blank=True, max_length=20, null=True)),
                ('rider_Pedestrian', models.CharField(blank=True, max_length=15, null=True)),
                ('basic_Skills', models.DateField(blank=True, null=True)),
                ('specific_Job', models.DateField(blank=True, null=True)),
                ('refresher_Test', models.DateField(blank=True, null=True)),
                ('familiarisation', models.DateField(blank=True, null=True)),
                ('theory', models.DateField(blank=True, null=True)),
                ('pre_Shift', models.DateField(blank=True, null=True)),
                ('manoeuvring', models.CharField(blank=True, max_length=5, null=True)),
                ('chicane', models.CharField(blank=True, max_length=5, null=True)),
                ('low_Level', models.CharField(blank=True, max_length=5, null=True)),
                ('eye_Level', models.CharField(blank=True, max_length=5, null=True)),
                ('high_Level', models.CharField(blank=True, max_length=5, null=True)),
                ('vert_Face', models.CharField(blank=True, max_length=5, null=True)),
                ('sop', models.CharField(blank=True, max_length=5, null=True)),
                ('fts', models.CharField(blank=True, max_length=5, null=True)),
                ('vehicle_Shovel', models.CharField(blank=True, max_length=5, null=True)),
                ('ramps', models.CharField(blank=True, max_length=5, null=True)),
                ('attachments_Initial', models.CharField(blank=True, max_length=5, null=True)),
                ('special_Application', models.CharField(blank=True, max_length=5, null=True)),
                ('pre_Use_Test', models.CharField(blank=True, max_length=5, null=True)),
                ('final_Grading', models.CharField(blank=True, max_length=1, null=True)),
                ('instructor_Comments', models.CharField(blank=True, max_length=1000, null=True)),
                ('theory_Test_Date', models.DateField(blank=True, null=True)),
                ('theory_Paper_Number', models.CharField(blank=True, max_length=10, null=True)),
                ('e_testDate', models.DateField(blank=True, null=True)),
                ('machine_Make', models.CharField(blank=True, max_length=30, null=True)),
                ('e_abaCategory', models.CharField(blank=True, max_length=30, null=True)),
                ('preUseEM_CRP', models.BooleanField()),
                ('preUseEM_CRR', models.BooleanField()),
                ('preUseEM_CRTD', models.DateField(blank=True, null=True)),
                ('BO_testDate', models.DateField(blank=True, null=True)),
                ('BO_truckType', models.CharField(blank=True, max_length=30, null=True)),
                ('BO_truckModel', models.CharField(blank=True, max_length=30, null=True)),
                ('BO_liftHeight', models.CharField(blank=True, max_length=30, null=True)),
                ('BO_capacity', models.CharField(blank=True, max_length=30, null=True)),
                ('BO_attachments', models.CharField(blank=True, max_length=30, null=True)),
                ('training_Ratio', models.CharField(blank=True, max_length=30, null=True)),
                ('course_Timing', models.CharField(blank=True, max_length=30, null=True)),
                ('instructorAdditionalComments', models.CharField(blank=True, max_length=3000, null=True)),
                ('md_1', models.BooleanField()),
                ('md_2', models.BooleanField()),
                ('md_3', models.BooleanField()),
                ('md_4', models.BooleanField()),
                ('md_5', models.BooleanField()),
                ('md_6', models.BooleanField()),
                ('md_7', models.BooleanField()),
                ('penalty_1', models.IntegerField(blank=True, null=True)),
                ('penalty_2', models.IntegerField(blank=True, null=True)),
                ('penalty_3', models.IntegerField(blank=True, null=True)),
                ('penalty_4', models.IntegerField(blank=True, null=True)),
                ('penalty_5', models.IntegerField(blank=True, null=True)),
                ('penalty_6', models.IntegerField(blank=True, null=True)),
                ('penalty_7', models.IntegerField(blank=True, null=True)),
                ('penalty_8', models.IntegerField(blank=True, null=True)),
                ('penalty_9', models.IntegerField(blank=True, null=True)),
                ('penalty_10', models.IntegerField(blank=True, null=True)),
                ('penalty_11', models.IntegerField(blank=True, null=True)),
                ('penalty_12', models.IntegerField(blank=True, null=True)),
                ('penalty_13', models.IntegerField(blank=True, null=True)),
                ('penalty_14', models.IntegerField(blank=True, null=True)),
                ('penalty_15', models.IntegerField(blank=True, null=True)),
                ('penalty_16', models.IntegerField(blank=True, null=True)),
                ('penalty_17', models.IntegerField(blank=True, null=True)),
                ('penalty_18', models.IntegerField(blank=True, null=True)),
                ('penalty_19', models.IntegerField(blank=True, null=True)),
                ('penalty_20', models.IntegerField(blank=True, null=True)),
                ('penalty_21', models.IntegerField(blank=True, null=True)),
                ('penalty_22', models.IntegerField(blank=True, null=True)),
                ('penalty_23', models.IntegerField(blank=True, null=True)),
                ('penalty_24', models.IntegerField(blank=True, null=True)),
                ('penalty_25', models.IntegerField(blank=True, null=True)),
                ('penalty_26', models.IntegerField(blank=True, null=True)),
                ('penalty_27', models.IntegerField(blank=True, null=True)),
                ('penalty_28', models.IntegerField(blank=True, null=True)),
                ('penalty_29', models.IntegerField(blank=True, null=True)),
                ('penalty_30', models.IntegerField(blank=True, null=True)),
                ('penalty_31', models.IntegerField(blank=True, null=True)),
                ('penalty_32', models.IntegerField(blank=True, null=True)),
                ('penalty_33', models.IntegerField(blank=True, null=True)),
                ('penalty_34', models.IntegerField(blank=True, null=True)),
                ('penalty_35', models.IntegerField(blank=True, null=True)),
                ('penalty_36', models.IntegerField(blank=True, null=True)),
                ('penalty_37', models.IntegerField(blank=True, null=True)),
                ('d1_JS', models.CharField(blank=True, max_length=1, null=True)),
                ('d1_SD', models.CharField(blank=True, max_length=1, null=True)),
                ('d1_LC', models.CharField(blank=True, max_length=1, null=True)),
                ('d1_M', models.CharField(blank=True, max_length=1, null=True)),
                ('d1_SA', models.CharField(blank=True, max_length=1, null=True)),
                ('d2_JS', models.CharField(blank=True, max_length=1, null=True)),
                ('d2_SD', models.CharField(blank=True, max_length=1, null=True)),
                ('d2_LC', models.CharField(blank=True, max_length=1, null=True)),
                ('d2_M', models.CharField(blank=True, max_length=1, null=True)),
                ('d2_SA', models.CharField(blank=True, max_length=1, null=True)),
                ('d3_JS', models.CharField(blank=True, max_length=1, null=True)),
                ('d3_SD', models.CharField(blank=True, max_length=1, null=True)),
                ('d3_LC', models.CharField(blank=True, max_length=1, null=True)),
                ('d3_M', models.CharField(blank=True, max_length=1, null=True)),
                ('d3_SA', models.CharField(blank=True, max_length=1, null=True)),
                ('d4_JS', models.CharField(blank=True, max_length=1, null=True)),
                ('d4_SD', models.CharField(blank=True, max_length=1, null=True)),
                ('d4_LC', models.CharField(blank=True, max_length=1, null=True)),
                ('d4_M', models.CharField(blank=True, max_length=1, null=True)),
                ('d4_SA', models.CharField(blank=True, max_length=1, null=True)),
                ('d5_JS', models.CharField(blank=True, max_length=1, null=True)),
                ('d5_SD', models.CharField(blank=True, max_length=1, null=True)),
                ('d5_LC', models.CharField(blank=True, max_length=1, null=True)),
                ('d5_M', models.CharField(blank=True, max_length=1, null=True)),
                ('d5_SA', models.CharField(blank=True, max_length=1, null=True)),
                ('mark_1', models.CharField(blank=True, max_length=3, null=True)),
                ('question_1', models.CharField(blank=True, max_length=3, null=True)),
                ('mark_2', models.CharField(blank=True, max_length=3, null=True)),
                ('question_2', models.CharField(blank=True, max_length=3, null=True)),
                ('mark_3', models.CharField(blank=True, max_length=3, null=True)),
                ('question_3', models.CharField(blank=True, max_length=3, null=True)),
                ('mark_4', models.CharField(blank=True, max_length=3, null=True)),
                ('question_4', models.CharField(blank=True, max_length=3, null=True)),
                ('mark_5', models.CharField(blank=True, max_length=3, null=True)),
                ('question_5', models.CharField(blank=True, max_length=3, null=True)),
                ('mark_6', models.CharField(blank=True, max_length=3, null=True)),
                ('question_6', models.CharField(blank=True, max_length=3, null=True)),
                ('mark_7', models.CharField(blank=True, max_length=3, null=True)),
                ('question_7', models.CharField(blank=True, max_length=3, null=True)),
                ('mark_8', models.CharField(blank=True, max_length=3, null=True)),
                ('question_8', models.CharField(blank=True, max_length=3, null=True)),
                ('mark_9', models.CharField(blank=True, max_length=3, null=True)),
                ('question_9', models.CharField(blank=True, max_length=3, null=True)),
                ('mark_10', models.CharField(blank=True, max_length=3, null=True)),
                ('question_10', models.CharField(blank=True, max_length=3, null=True)),
                ('mark_11', models.CharField(blank=True, max_length=3, null=True)),
                ('question_11', models.CharField(blank=True, max_length=3, null=True)),
                ('mark_12', models.CharField(blank=True, max_length=3, null=True)),
                ('question_12', models.CharField(blank=True, max_length=3, null=True)),
                ('mark_13', models.CharField(blank=True, max_length=3, null=True)),
                ('question_13', models.CharField(blank=True, max_length=3, null=True)),
                ('mark_14', models.CharField(blank=True, max_length=3, null=True)),
                ('question_14', models.CharField(blank=True, max_length=3, null=True)),
                ('mark_15', models.CharField(blank=True, max_length=3, null=True)),
                ('question_15', models.CharField(blank=True, max_length=3, null=True)),
                ('mark_16', models.CharField(blank=True, max_length=3, null=True)),
                ('question_16', models.CharField(blank=True, max_length=3, null=True)),
                ('mark_17', models.CharField(blank=True, max_length=3, null=True)),
                ('question_17', models.CharField(blank=True, max_length=3, null=True)),
                ('mark_18', models.CharField(blank=True, max_length=3, null=True)),
                ('question_18', models.CharField(blank=True, max_length=3, null=True)),
                ('mark_19', models.CharField(blank=True, max_length=3, null=True)),
                ('question_19', models.CharField(blank=True, max_length=3, null=True)),
                ('mark_20', models.CharField(blank=True, max_length=3, null=True)),
                ('question_20', models.CharField(blank=True, max_length=3, null=True)),
                ('mark_21', models.CharField(blank=True, max_length=3, null=True)),
                ('question_21', models.CharField(blank=True, max_length=300, null=True)),
                ('mark_22', models.CharField(blank=True, max_length=3, null=True)),
                ('question_22', models.CharField(blank=True, max_length=300, null=True)),
                ('mark_23', models.CharField(blank=True, max_length=3, null=True)),
                ('question_23', models.CharField(blank=True, max_length=300, null=True)),
                ('mark_24', models.CharField(blank=True, max_length=3, null=True)),
                ('question_24', models.CharField(blank=True, max_length=300, null=True)),
                ('mark_25', models.CharField(blank=True, max_length=3, null=True)),
                ('question_25', models.CharField(blank=True, max_length=300, null=True)),
                ('preUseEM_1', models.CharField(blank=True, max_length=10, null=True)),
                ('preUseEM_2', models.CharField(blank=True, max_length=10, null=True)),
                ('preUseEM_3', models.CharField(blank=True, max_length=10, null=True)),
                ('preUseEM_4', models.CharField(blank=True, max_length=10, null=True)),
                ('preUseEM_5', models.CharField(blank=True, max_length=10, null=True)),
                ('preUseEM_6', models.CharField(blank=True, max_length=10, null=True)),
                ('preUseEM_7', models.CharField(blank=True, max_length=10, null=True)),
                ('preUseEM_8', models.CharField(blank=True, max_length=10, null=True)),
                ('preUseEM_9', models.CharField(blank=True, max_length=10, null=True)),
                ('preUseEM_10', models.CharField(blank=True, max_length=10, null=True)),
                ('preUseEM_11', models.CharField(blank=True, max_length=10, null=True)),
                ('preUseEM_12', models.CharField(blank=True, max_length=10, null=True)),
                ('preUseEM_13', models.CharField(blank=True, max_length=10, null=True)),
                ('preUseEM_14', models.CharField(blank=True, max_length=10, null=True)),
                ('preUseEM_15', models.CharField(blank=True, max_length=10, null=True)),
                ('preUseEM_16', models.CharField(blank=True, max_length=10, null=True)),
                ('preUseEM_17', models.CharField(blank=True, max_length=10, null=True)),
                ('preUseEM_18', models.CharField(blank=True, max_length=10, null=True)),
                ('preUseEM_19', models.CharField(blank=True, max_length=10, null=True)),
                ('preUseEM_20', models.CharField(blank=True, max_length=10, null=True)),
                ('preUseEM_21', models.CharField(blank=True, max_length=10, null=True)),
                ('preUseEM_22', models.CharField(blank=True, max_length=10, null=True)),
                ('BO_D1', models.DateField(blank=True, null=True)),
                ('BO_D2', models.DateField(blank=True, null=True)),
                ('BO_D3', models.DateField(blank=True, null=True)),
                ('BO_D4', models.DateField(blank=True, null=True)),
                ('BO_D5', models.DateField(blank=True, null=True)),
                ('BO_D6', models.DateField(blank=True, null=True)),
                ('BO_D7', models.DateField(blank=True, null=True)),
                ('BO_D8', models.DateField(blank=True, null=True)),
                ('BO_D9', models.DateField(blank=True, null=True)),
                ('BO_D10', models.DateField(blank=True, null=True)),
                ('BO_D11', models.DateField(blank=True, null=True)),
                ('BO_D12', models.DateField(blank=True, null=True)),
                ('BO_D13', models.DateField(blank=True, null=True)),
                ('BO_D14', models.DateField(blank=True, null=True)),
                ('BO_D15', models.DateField(blank=True, null=True)),
                ('BO_D16', models.DateField(blank=True, null=True)),
                ('BO_D17', models.DateField(blank=True, null=True)),
                ('BO_D18', models.DateField(blank=True, null=True)),
                ('BO_D19', models.DateField(blank=True, null=True)),
                ('BO_D20', models.DateField(blank=True, null=True)),
                ('BO_D21', models.DateField(blank=True, null=True)),
                ('BO_D22', models.DateField(blank=True, null=True)),
                ('BO_D23', models.DateField(blank=True, null=True)),
                ('BO_D24', models.DateField(blank=True, null=True)),
                ('eval_1', models.CharField(choices=[('review_1', '1'), ('review_2', '2'), ('review_3', '3'), ('review_4', '4'), ('review_5', '5')], default=0, max_length=10, null=True)),
                ('eval_2', models.CharField(choices=[('review_1', '1'), ('review_2', '2'), ('review_3', '3'), ('review_4', '4'), ('review_5', '5')], default=0, max_length=10, null=True)),
                ('eval_3', models.CharField(choices=[('review_1', '1'), ('review_2', '2'), ('review_3', '3'), ('review_4', '4'), ('review_5', '5')], default=0, max_length=10, null=True)),
                ('eval_4', models.CharField(choices=[('review_1', '1'), ('review_2', '2'), ('review_3', '3'), ('review_4', '4'), ('review_5', '5')], default=0, max_length=10, null=True)),
                ('eval_5', models.CharField(choices=[('review_1', '1'), ('review_2', '2'), ('review_3', '3'), ('review_4', '4'), ('review_5', '5')], default=0, max_length=10, null=True)),
                ('eval_6', models.CharField(choices=[('review_1', '1'), ('review_2', '2'), ('review_3', '3'), ('review_4', '4'), ('review_5', '5')], default=0, max_length=10, null=True)),
                ('eval_7', models.CharField(choices=[('review_1', '1'), ('review_2', '2'), ('review_3', '3'), ('review_4', '4'), ('review_5', '5')], default=0, max_length=10, null=True)),
                ('eval_8', models.CharField(choices=[('review_1', '1'), ('review_2', '2'), ('review_3', '3'), ('review_4', '4'), ('review_5', '5')], default=0, max_length=10, null=True)),
                ('eval_9', models.CharField(choices=[('review_1', '1'), ('review_2', '2'), ('review_3', '3'), ('review_4', '4'), ('review_5', '5')], default=0, max_length=10, null=True)),
                ('eval_10', models.CharField(blank=True, max_length=300, null=True)),
                ('eval_11', models.CharField(blank=True, max_length=300, null=True)),
                ('eval_12', models.CharField(blank=True, max_length=300, null=True)),
                ('company_Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shovelCustomer', to='customers.customers')),
                ('course_Number', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shovelCourse', to='courses.courses')),
                ('instructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shovelInstructor', to=settings.AUTH_USER_MODEL)),
                ('instructor_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shovelInstructor2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]