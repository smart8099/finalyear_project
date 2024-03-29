# Generated by Django 4.2.5 on 2023-10-01 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opd', '0008_patientopdvisit_status'),
        ('lab', '0001_labrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabTestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_value', models.CharField(max_length=100)),
                ('lab_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lab_test_results', to='lab.labrequest')),
                ('lab_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab.labtestsavailable')),
                ('opd_visit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='opd.patientopdvisit')),
            ],
        ),
    ]
