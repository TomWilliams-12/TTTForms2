# Generated by Django 3.2.7 on 2022-02-20 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aw', '0003_auto_20220220_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aw',
            old_name='finalGrading',
            new_name='d1_JS',
        ),
        migrations.RenameField(
            model_name='aw',
            old_name='jobSafety',
            new_name='d1_M',
        ),
        migrations.RenameField(
            model_name='aw',
            old_name='motivation',
            new_name='d1_SA',
        ),
        migrations.RenameField(
            model_name='aw',
            old_name='safetyAttitude',
            new_name='d1_SD',
        ),
        migrations.RenameField(
            model_name='aw',
            old_name='skillDex',
            new_name='final_Grading',
        ),
        migrations.RenameField(
            model_name='aw',
            old_name='instructorComments',
            new_name='instructor_Comments',
        ),
        migrations.RenameField(
            model_name='aw',
            old_name='theoryPaperNumber',
            new_name='theory_Paper_Number',
        ),
        migrations.RenameField(
            model_name='aw',
            old_name='theoryTestDate',
            new_name='theory_Test_Date',
        ),
    ]
