# Generated by Django 3.2.7 on 2023-09-15 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hpisApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientreg',
            name='contact_number',
        ),
        migrations.AlterField(
            model_name='patientreg',
            name='address',
            field=models.CharField(max_length=50),
        ),
    ]
