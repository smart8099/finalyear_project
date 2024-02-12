from django.db import models
from opd.models import Patient
from model_utils.models import TimeStampedModel
from opd.models import PatientOPDVisit

# Create your models here.
class LabTestsAvailable(models.Model):
    lab_test_name = models.CharField(max_length=100)

    def __str__(self):
        return self.lab_test_name


class LabRequest(TimeStampedModel):
    STATUS_CHOICES = (
        ('Lab Requested', 'Lab Requested'),
        ('Lab Completed', 'Lab Completed'),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    opd_visit = models.OneToOneField(PatientOPDVisit,on_delete=models.CASCADE)
    lab_tests = models.ManyToManyField(LabTestsAvailable)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Lab Requested')

    def __str__(self):
        return f"Lab Request for {self.patient.patient_clinic_id} on {self.opd_visit.created}"


class LabTestResult(models.Model):
    lab_request = models.ForeignKey(LabRequest, on_delete=models.CASCADE, related_name='lab_test_results')
    lab_test = models.ForeignKey(LabTestsAvailable, on_delete=models.CASCADE)
    result_value = models.CharField(max_length=100)
    opd_visit = models.ForeignKey(PatientOPDVisit, on_delete=models.CASCADE)

    def __str__(self):
        return f"Lab Test Result for {self.lab_request.id}"