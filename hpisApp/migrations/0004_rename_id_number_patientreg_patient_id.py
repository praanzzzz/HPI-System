# Generated by Django 3.2.7 on 2023-09-15 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hpisApp', '0003_rename_student_number_patientreg_id_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientreg',
            old_name='id_number',
            new_name='patient_id',
        ),
    ]
