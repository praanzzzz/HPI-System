# Generated by Django 3.2.7 on 2023-09-18 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hpisApp', '0009_medhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medhistory',
            name='bp',
            field=models.CharField(max_length=10),
        ),
    ]
