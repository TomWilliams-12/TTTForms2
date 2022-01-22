# Generated by Django 3.2.7 on 2022-01-03 09:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsignature.fields


class Migration(migrations.Migration):

    replaces = [('cbr', '0001_initial'), ('cbr', '0002_auto_20220102_1638'), ('cbr', '0003_auto_20220102_1639'), ('cbr', '0004_auto_20220102_1639'), ('cbr', '0005_auto_20220102_1641'), ('cbr', '0006_auto_20220102_1642'), ('cbr', '0007_auto_20220102_1645'), ('cbr', '0008_auto_20220102_1646'), ('cbr', '0009_auto_20220102_1650'), ('cbr', '0010_auto_20220102_1907'), ('cbr', '0011_auto_20220102_1908')]

    initial = True

    dependencies = [
        ('customers', '0003_auto_20211102_1823'),
        ('courses', '0002_auto_20211024_1554'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cbr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_Name', models.CharField(max_length=50)),
                ('course_Type', models.CharField(blank=True, max_length=50, null=True)),
                ('venue', models.CharField(blank=True, max_length=30, null=True)),
                ('start_Date', models.DateField(blank=True, null=True)),
                ('finish_Date', models.DateField(blank=True, null=True)),
                ('candidate_Initial', models.CharField(blank=True, max_length=5, null=True)),
                ('candidate_Checkbox', models.BooleanField()),
                ('candidate_Signature', jsignature.fields.JSignatureField(blank=True, null=True)),
                ('candidate_DOB', models.DateField(blank=True, null=True)),
                ('candidateTopsId', models.CharField(blank=True, max_length=20, null=True)),
                ('candidate_NIN', models.CharField(blank=True, max_length=9, null=True)),
                ('machine_Type', models.CharField(blank=True, max_length=30, null=True)),
                ('machine_Group', models.CharField(blank=True, max_length=5, null=True)),
                ('machine_Make_Model', models.CharField(blank=True, max_length=50, null=True)),
                ('machine_Capacity', models.IntegerField(blank=True, null=True)),
                ('machine_Load_Centre', models.IntegerField(blank=True, null=True)),
                ('machine_Test_Lift_Height', models.IntegerField(blank=True, null=True)),
                ('machine_Attachments', models.CharField(blank=True, max_length=20, null=True)),
                ('machine_Motive_Power', models.CharField(blank=True, max_length=20, null=True)),
                ('courseTypeN', models.BooleanField()),
                ('courseTypeE', models.BooleanField()),
                ('courseTypeC', models.BooleanField()),
                ('courseTypeSF', models.BooleanField()),
                ('training_Ratio', models.CharField(blank=True, max_length=10, null=True)),
                ('course_Duration', models.FloatField(blank=True, null=True)),
                ('basic_Skills', models.DateField(blank=True, null=True)),
                ('theory', models.DateField(blank=True, null=True)),
                ('pre_Use', models.DateField(blank=True, null=True)),
                ('refresher_Test', models.DateField(blank=True, null=True)),
                ('familiarisation', models.DateField(blank=True, null=True)),
                ('specific_Job', models.DateField(blank=True, null=True)),
                ('final_Grading', models.CharField(blank=True, max_length=1, null=True)),
                ('pre_Use_Test', models.CharField(blank=True, max_length=10, null=True)),
                ('overall_Result', models.CharField(blank=True, max_length=10, null=True)),
                ('instructor_Comments', models.CharField(blank=True, max_length=1000, null=True)),
                ('set_Time', models.IntegerField(blank=True, null=True)),
                ('start_Time', models.TimeField(blank=True, null=True)),
                ('finish_Time', models.TimeField(blank=True, null=True)),
                ('restriction_Detail', models.CharField(blank=True, max_length=500, null=True)),
                ('testPaperReference', models.CharField(blank=True, max_length=10, null=True)),
                ('ot_12_L', models.BooleanField()),
                ('ot_12_M', models.BooleanField()),
                ('ot_12_H', models.BooleanField()),
                ('ot_13_L', models.BooleanField()),
                ('ot_13_M', models.BooleanField()),
                ('ot_13_H', models.BooleanField()),
                ('ot_14_L', models.BooleanField()),
                ('ot_14_M', models.BooleanField()),
                ('ot_14_H', models.BooleanField()),
                ('ot_17_T', models.BooleanField()),
                ('ot_17_P', models.BooleanField()),
                ('ot_18_T', models.BooleanField()),
                ('ot_18_P', models.BooleanField()),
                ('ot_19_PU', models.BooleanField()),
                ('ot_19_T', models.BooleanField()),
                ('ot_19_P', models.BooleanField()),
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
                ('md_1', models.BooleanField()),
                ('md_2', models.BooleanField()),
                ('md_3', models.BooleanField()),
                ('md_4', models.BooleanField()),
                ('md_5', models.BooleanField()),
                ('md_6', models.BooleanField()),
                ('md_7', models.BooleanField()),
                ('check_1_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_1_cr', models.BooleanField()),
                ('check_2_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_2_cr', models.BooleanField()),
                ('check_3_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_3_cr', models.BooleanField()),
                ('check_4_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_4_cr', models.BooleanField()),
                ('check_5_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_5_cr', models.BooleanField()),
                ('check_6_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_6_cr', models.BooleanField()),
                ('check_7_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_7_cr', models.BooleanField()),
                ('check_8_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_8_cr', models.BooleanField()),
                ('check_9_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_9_cr', models.BooleanField()),
                ('check_10_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_10_cr', models.BooleanField()),
                ('check_11_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_11_cr', models.BooleanField()),
                ('check_12_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_12_cr', models.BooleanField()),
                ('check_13_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_13_cr', models.BooleanField()),
                ('check_14_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_14_cr', models.BooleanField()),
                ('check_15_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_15_cr', models.BooleanField()),
                ('check_16_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_16_cr', models.BooleanField()),
                ('check_17_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_17_cr', models.BooleanField()),
                ('check_18_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_18_cr', models.BooleanField()),
                ('check_19_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_19_cr', models.BooleanField()),
                ('check_20_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_20_cr', models.BooleanField()),
                ('check_21_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_21_cr', models.BooleanField()),
                ('check_22_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_22_cr', models.BooleanField()),
                ('check_23_cc', models.CharField(blank=True, max_length=5, null=True)),
                ('check_23_cr', models.BooleanField()),
                ('d1_SD', models.CharField(blank=True, max_length=1, null=True)),
                ('d1_RTI', models.CharField(blank=True, max_length=1, null=True)),
                ('d1_M', models.CharField(blank=True, max_length=1, null=True)),
                ('d1_SA', models.CharField(blank=True, max_length=1, null=True)),
                ('d2_SD', models.CharField(blank=True, max_length=1, null=True)),
                ('d2_RTI', models.CharField(blank=True, max_length=1, null=True)),
                ('d2_M', models.CharField(blank=True, max_length=1, null=True)),
                ('d2_SA', models.CharField(blank=True, max_length=1, null=True)),
                ('d3_SD', models.CharField(blank=True, max_length=1, null=True)),
                ('d3_RTI', models.CharField(blank=True, max_length=1, null=True)),
                ('d3_M', models.CharField(blank=True, max_length=1, null=True)),
                ('d3_SA', models.CharField(blank=True, max_length=1, null=True)),
                ('d4_SD', models.CharField(blank=True, max_length=1, null=True)),
                ('d4_RTI', models.CharField(blank=True, max_length=1, null=True)),
                ('d4_M', models.CharField(blank=True, max_length=1, null=True)),
                ('d4_SA', models.CharField(blank=True, max_length=1, null=True)),
                ('d5_SD', models.CharField(blank=True, max_length=1, null=True)),
                ('d5_RTI', models.CharField(blank=True, max_length=1, null=True)),
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
                ('ot_1', models.CharField(blank=True, max_length=10, null=True)),
                ('ot_2', models.CharField(blank=True, max_length=10, null=True)),
                ('ot_3', models.CharField(blank=True, max_length=10, null=True)),
                ('ot_4', models.CharField(blank=True, max_length=10, null=True)),
                ('ot_5', models.CharField(blank=True, max_length=10, null=True)),
                ('ot_6', models.CharField(blank=True, max_length=10, null=True)),
                ('ot_7', models.CharField(blank=True, max_length=10, null=True)),
                ('ot_8', models.CharField(blank=True, max_length=10, null=True)),
                ('ot_9', models.CharField(blank=True, max_length=10, null=True)),
                ('ot_10', models.CharField(blank=True, max_length=10, null=True)),
                ('ot_11', models.CharField(blank=True, max_length=10, null=True)),
                ('ot_12', models.CharField(blank=True, max_length=10, null=True)),
                ('ot_13', models.CharField(blank=True, max_length=10, null=True)),
                ('ot_14', models.CharField(blank=True, max_length=10, null=True)),
                ('ot_15', models.CharField(blank=True, max_length=10, null=True)),
                ('ot_16', models.CharField(blank=True, max_length=10, null=True)),
                ('ot_17', models.CharField(blank=True, max_length=10, null=True)),
                ('ot_18', models.CharField(blank=True, max_length=10, null=True)),
                ('ot_19', models.CharField(blank=True, max_length=10, null=True)),
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
                ('company_Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer', to='customers.customers')),
                ('course_Number', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course', to='courses.courses')),
                ('instructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='instructor', to=settings.AUTH_USER_MODEL)),
                ('instructor_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='instructor2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]