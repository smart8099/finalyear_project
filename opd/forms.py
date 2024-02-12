from django import forms
from .models import Patient,PatientOPDVisit

class PatientRegistrationForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),  # Use 'date' type for HTML5 date input
    )

    religion = forms.ChoiceField(
        # choices=Patient.PATIENT_RELIGION,
        choices=[('', 'Select Religion')] + Patient.PATIENT_RELIGION,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_my_choice_field'}),

    )

    sex = forms.ChoiceField(
        choices=[('', 'Select Sex')] + Patient.GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_my_choice_field'}),

    )

    patient_type = forms.ChoiceField(
        choices=[('', 'Select Patient Type')] + Patient.PATIENT_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_my_choice_field'}),

    )

    race = forms.ChoiceField(
        choices=[('', 'Select Race')] + Patient.RACE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_my_choice_field'}),

    )

    marital_status = forms.ChoiceField(
        choices=[('', 'Select Marital Status')] + Patient.PATIENT_MARITAL_STATUS,
         widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_my_choice_field'}),

    )

    address_next_of_kin = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),  # Adjust the 'rows' value as needed
        label="Next of Kin's Address",
        required=False,  # Optional field
    )
    residential_address = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),  # Adjust the 'rows' value as needed
        label='Residential Address',
        required=False,  # Optional field
    )
    business_address = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),  # Adjust the 'rows' value as needed
        label='Business Address',
        required=False,  # Optional field
    )
    class Meta:
        model = Patient
        exclude = ['patient_clinic_id', 'created','modified','id']




class PatientOPDVisitsForm(forms.ModelForm):
    patient = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '00001'}),
        label='Patient Clinic ID'
    )

    temperature = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '37.5'}),
        label='Temperature'
    )

    pulse_rate = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '87bpm'}),
        label='Pulse Rate'
    )

    weight = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '37.5'}),
        label='Weight'
    )

    blood_pressure = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'e.g., 120/80', 'id': 'id_blood_pressure'}),
    )

    class Meta:
        model = PatientOPDVisit
        exclude = ['created','modified','id','status']


class PatientOPDVisitsWithClinicIDForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        patient_id = cleaned_data.get('patient_id')  # Assuming you have a field named 'patient_id' in your form
        print(f'the patient id is {patient_id}')
        try:
            patient = Patient.objects.get(patient_clinic_id=patient_id)
        except Patient.DoesNotExist:
            self.add_error('patient_id', 'Patient with this clinic ID does not exist.')

    # patient_id = forms.CharField()  # Add a clinic ID field
    patient_id = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'enter patient ID e.g. (00001)', 'id': 'id_patient_id'}),
        label='Patient ID'
    )
    temperature = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'enter temperature in C e.g. (37.5)'}),
        label='Temperature'
    )

    pulse_rate = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'enter pulse rate in bpm e.g. (87bpm)'}),
        label='Pulse Rate'
    )

    weight = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'enter weight in kg e.g. (50)'}),
        label='Weight'
    )

    blood_pressure = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'enter blood pressure in the format (120/80)', 'id': 'id_blood_pressure'}),
    )

    class Meta:
        model = PatientOPDVisit
        exclude = ['created', 'modified', 'id', 'patient','status']