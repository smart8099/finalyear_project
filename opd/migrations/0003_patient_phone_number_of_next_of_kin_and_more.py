# Generated by Django 4.2.5 on 2023-09-24 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opd', '0002_alter_patient_race'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='phone_number_of_next_of_kin',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_number',
            field=models.CharField(default='', max_length=11, unique=True),
        ),
    ]
