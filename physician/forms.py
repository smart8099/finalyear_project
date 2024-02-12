from django import forms
from .models import PhysicianDiagnostic

class PhysicianDiagnosticForm(forms.ModelForm):
    class Meta:
        model = PhysicianDiagnostic
        fields = ['symptoms', 'prescription', 'diagnosis']

    # symptoms = forms.CharField(
    #     widget=forms.Textarea(attrs={'rows':10,'column':10}),  # Adjust the 'rows' value as needed
    #     label='Residential Address',
    #     required=False,  # Optional field
    # )