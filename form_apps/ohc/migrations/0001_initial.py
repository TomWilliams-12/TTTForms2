# Generated by Django 3.2.7 on 2022-02-13 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsignature.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0002_auto_20211024_1554'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0004_customers_company_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ohc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('audit_Notes', models.CharField(blank=True, max_length=500, null=True)),
                ('audit_Completed', models.BooleanField(default=False)),
                ('has_Certificate', models.BooleanField(default=False)),
                ('machine_Motive_Power', models.CharField(blank=True, default='Electric', max_length=50, null=True)),
                ('machine_Type', models.CharField(blank=True, default='Overhead Crane', max_length=50, null=True)),
                ('candidateTopsId', models.CharField(blank=True, max_length=30, null=True)),
                ('courseTypeN', models.BooleanField(default=False)),
                ('courseTypeE', models.BooleanField(default=False)),
                ('courseTypeC', models.BooleanField(default=False)),
                ('courseTypeSF', models.BooleanField(default=False)),
                ('candidate_Name', models.CharField(blank=True, max_length=50, null=True)),
                ('course_Type', models.CharField(blank=True, max_length=50, null=True)),
                ('venue', models.CharField(blank=True, max_length=30, null=True)),
                ('start_Date', models.DateField(blank=True, null=True)),
                ('finish_Date', models.DateField(blank=True, null=True)),
                ('candidate_Initial', models.CharField(blank=True, max_length=5, null=True)),
                ('candidate_Checkbox', models.BooleanField()),
                ('signature', jsignature.fields.JSignatureField(blank=True, null=True)),
                ('organisation', models.CharField(blank=True, max_length=50, null=True)),
                ('machine_Make_Model', models.CharField(blank=True, max_length=50, null=True)),
                ('machine_Group', models.CharField(blank=True, max_length=20, null=True)),
                ('machine_Capacity', models.IntegerField(blank=True, null=True)),
                ('attachments', models.CharField(blank=True, max_length=20, null=True)),
                ('static_Travelling', models.CharField(blank=True, max_length=20, null=True)),
                ('set_Time', models.IntegerField(blank=True, null=True)),
                ('start_Time', models.TimeField(blank=True, null=True)),
                ('finish_Time', models.TimeField(blank=True, null=True)),
                ('testPass', models.BooleanField()),
                ('testFail', models.BooleanField()),
                ('testDate', models.DateField(blank=True, null=True)),
                ('candidate_DOB', models.DateField(blank=True, null=True)),
                ('courseTitle', models.CharField(blank=True, max_length=50, null=True)),
                ('course_Duration', models.CharField(blank=True, max_length=20, null=True)),
                ('crane_Make', models.CharField(blank=True, max_length=50, null=True)),
                ('crane_Model', models.CharField(blank=True, max_length=50, null=True)),
                ('capacity', models.CharField(blank=True, max_length=50, null=True)),
                ('group', models.CharField(blank=True, max_length=5, null=True)),
                ('lifting_Accessories', models.CharField(blank=True, max_length=50, null=True)),
                ('basic_Skills', models.DateField(blank=True, null=True)),
                ('specific_Job', models.DateField(blank=True, null=True)),
                ('refresher_Test', models.DateField(blank=True, null=True)),
                ('familiarisation', models.DateField(blank=True, null=True)),
                ('theory', models.DateField(blank=True, null=True)),
                ('pre_Shift', models.DateField(blank=True, null=True)),
                ('manoeuvring', models.CharField(blank=True, max_length=5, null=True)),
                ('sop', models.CharField(blank=True, max_length=5, null=True)),
                ('cs', models.CharField(blank=True, max_length=5, null=True)),
                ('vehicle_Loading', models.CharField(blank=True, max_length=5, null=True)),
                ('off_Loading', models.CharField(blank=True, max_length=5, null=True)),
                ('attachments2', models.CharField(blank=True, max_length=5, null=True)),
                ('signalling_Communication', models.CharField(blank=True, max_length=5, null=True)),
                ('special_Application', models.CharField(blank=True, max_length=50, null=True)),
                ('pre_Use_Test', models.CharField(blank=True, max_length=5, null=True)),
                ('final_Grading', models.CharField(blank=True, max_length=1, null=True)),
                ('instructor_Comments', models.CharField(blank=True, max_length=1000, null=True)),
                ('theory_Test_Date', models.DateField(blank=True, null=True)),
                ('theory_Paper_Number', models.CharField(blank=True, max_length=10, null=True)),
                ('e_testDate', models.DateField(blank=True, null=True)),
                ('e_truckType', models.CharField(blank=True, max_length=30, null=True)),
                ('e_model', models.CharField(blank=True, max_length=30, null=True)),
                ('preUseEM_CRP', models.BooleanField()),
                ('preUseEM_CRR', models.BooleanField()),
                ('preUseEM_CRTD', models.DateField(blank=True, null=True)),
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
                ('md_8', models.BooleanField()),
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
                ('company_Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ohcCustomer', to='customers.customers')),
                ('course_Number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ohcCourse', to='courses.courses')),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ohcInstructor', to=settings.AUTH_USER_MODEL)),
                ('instructor_2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ohcInstructor2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
