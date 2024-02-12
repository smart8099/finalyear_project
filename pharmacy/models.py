from django.db import models
from model_utils.models import TimeStampedModel
from opd.models import Patient,PatientOPDVisit


class DrugRequest(models.Model):
    STATUS_CHOICES = (
        ('Drugs Requested', 'Drugs Requested'),
        ('Presciption Given', 'Presciption Given'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    opd_visit = models.OneToOneField(PatientOPDVisit, on_delete=models.CASCADE)
    drugs_requested = models.TextField(verbose_name='Drugs Requested')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Drugs Requested')

    def __str__(self):
        return f'Drug Request to {self.patient_id} on {self.opd_visit.created}'



