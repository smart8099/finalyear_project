from django.db import migrations

def populate_lab_tests(apps, schema_editor):
    LabTestsAvailable = apps.get_model('lab', 'LabTestsAvailable')
    common_tests = [
        'Full Blood Count',
        'Liver function test',
        'Kidney function test',
        'Thyroid function test',
        'Lipid/Cholesterol test',
        'Hormone assay (Serum Prolactin, Leutinizing hormone, Follicle stimulating hormone)',
        'Glycated Haemoglobin (HbA1c)',
        'Prostate Specific Antigen test',
        'Immunoassay for SARS COV 2 (Covid 19 test)',
        'Genotyping (electrophoresis for sickle cell genotype)',
        'Blood film comments',
        'D-Dimers',
        'Cardiac enzymes',
        'Alpha-fetoprotein',
        'Serum Beta HCG',
        'Serum Uric',
    ]

    lab_tests_to_create = [LabTestsAvailable(lab_test_name=test_name) for test_name in common_tests]
    LabTestsAvailable.objects.bulk_create(lab_tests_to_create)



class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_lab_tests),
    ]
