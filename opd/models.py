from django.db import models
from model_utils.models import TimeStampedModel
from datetime import date
class Patient(TimeStampedModel):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    PATIENT_TYPE_CHOICES = [
        ('Student', 'Student'),
        ('Staff', 'Staff'),
        ('Other','Other')
    ]

    PATIENT_RELIGION = [
        ('ISLAM', 'ISLAM'),
        ('CHRISTIANITY', 'CHRISTIANITY'),
        ('OTHER','OTHER')
    ]

    RACE_CHOICES = [
        ('Black/African American', 'Black/African American'),
        ('Asian', 'Asian'),
        ('White', 'White'),
        ('Other', 'Other'),
    ]

    PATIENT_MARITAL_STATUS = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
        ('Other', 'Other'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    index_or_staff_id = models.CharField(max_length=30,unique=True,blank=True)
    email = models.EmailField(unique=True,blank=True, null=True)
    phone_number = models.CharField(max_length=11, unique=True, default="")
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=15,choices=PATIENT_MARITAL_STATUS)
    tribe = models.CharField(max_length=100,null=True,blank=True)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100,blank=True,null=True)
    patient_type = models.CharField(max_length=7, choices=PATIENT_TYPE_CHOICES)
    residential_address = models.TextField(null=True, blank=True)
    business_address = models.TextField(null=True, blank=True)
    next_of_kin = models.CharField(max_length=100,null=True,blank=True)
    phone_number_of_next_of_kin = models.CharField(max_length=11,null=True,blank=True)
    address_next_of_kin = models.TextField(null=True, blank=True)
    occupation = models.CharField(max_length=100,null=True,blank=100)
    race = models.CharField(max_length=50,choices=RACE_CHOICES)
    religion = models.CharField(max_length=40,choices=PATIENT_RELIGION)
    patient_clinic_id = models.CharField(max_length=10,unique=True)


    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return age


    def __str__(self):
        return f"{self.first_name} {self.patient_clinic_id}"


    def save(self, *args, **kwargs):
        if not self.patient_clinic_id:
            last_patient = Patient.objects.last()  # Get the last patient in the database
            if last_patient:
                last_id = int(last_patient.patient_clinic_id)
                self.patient_clinic_id = str(last_id + 1).zfill(5)
            else:
                    self.patient_clinic_id = '00001'
        super(Patient, self).save(*args, **kwargs)




class PatientOPDVisit(TimeStampedModel):
    STATUS_CHOICES = (
        ('Pending OPD', 'Pending OPD'),
        ('Seen Physician', 'Seen Physician'),
    )
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='patient_visits')
    temperature = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    blood_pressure = models.CharField(max_length=20)
    pulse_rate = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending OPD')

    def __str__(self):
        return f"OPD Visit for {self.patient.first_name} {self.patient.last_name} on {self.created}"

    class Meta:
        ordering = ['-created', '-modified']