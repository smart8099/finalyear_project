# Generated by Django 4.2.5 on 2023-10-05 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('physician', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physiciandiagnostic',
            name='diagnosis',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='physiciandiagnostic',
            name='prescription',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='physiciandiagnostic',
            name='symptoms',
            field=models.TextField(),
        ),
    ]