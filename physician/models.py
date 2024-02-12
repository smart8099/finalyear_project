from django.db import models
from opd.models import PatientOPDVisit,Patient  # Import the OPDVisit model
from model_utils.models import TimeStampedModel

class PhysicianDiagnostic(TimeStampedModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    opd_visit = models.OneToOneField(PatientOPDVisit, on_delete=models.CASCADE)
    symptoms = models.TextField(blank=False)
    prescription = models.TextField(blank=False)
    diagnosis = models.TextField(blank=False)

    def __str__(self):
        return f"Diagnostic for {self.patient_id} on {self.opd_visit.created}"