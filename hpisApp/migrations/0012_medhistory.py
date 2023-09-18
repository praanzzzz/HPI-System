# Generated by Django 3.2.7 on 2023-09-18 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hpisApp', '0011_delete_medhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medhis_id', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('doctor', models.CharField(max_length=50)),
                ('bp', models.CharField(max_length=10)),
                ('diagnosis', models.CharField(max_length=50)),
                ('medication', models.CharField(max_length=50)),
            ],
        ),
    ]
