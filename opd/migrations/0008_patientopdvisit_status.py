# Generated by Django 4.2.5 on 2023-09-29 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opd', '0007_patientopdvisit'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientopdvisit',
            name='status',
            field=models.CharField(choices=[('Pending OPD', 'Pending OPD'), ('Seen Physician', 'Seen Physician')], default='Pending OPD', max_length=20),
        ),
    ]