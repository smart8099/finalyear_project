from django.shortcuts import render,redirect
from .forms import PatientRegistrationForm, PatientOPDVisitsForm, PatientOPDVisitsWithClinicIDForm
from django.contrib import messages
from .models import Patient,PatientOPDVisit
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.db.models import Q
from hyperX_core.utils import auth_permission
from django.contrib.auth.decorators import user_passes_test



@user_passes_test(auth_permission.is_nurse)
def opd_homepage(request):
    return render(request,template_name='opd/opd_base.html')

@user_passes_test(auth_permission.is_record_manager)
def record_manager_homepage(request):
    return render(request,template_name='opd/record_manager_base.html')
@user_passes_test(auth_permission.is_record_manager)
def add_new_patient(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            patient = form.save()
            messages.success(request,f'Patient Record successfully created')

            form = PatientRegistrationForm()
        else:
            messages.error(request, 'Form submission failed. Please correct the errors below.')

    else:
        form = PatientRegistrationForm()

    return render(request, 'opd/register_patient.html',{'form': form})

@user_passes_test(auth_permission.is_record_manager)
def edit_patient(request, patient_id):
    try:
        patient = Patient.objects.get(pk=patient_id)
    except Patient.DoesNotExist:
        messages.error(request,'patient does not exist')
        return redirect('patient_list')

    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request,f'Patient Record successfully Updated')
            return redirect('patient_list')
        else:
            messages.error(request, 'Form submission failed. Please correct the errors below.')
    else:
        form = PatientRegistrationForm(instance=patient)

    return render(request, 'opd/edit_patient_record.html', {'form': form, 'patient': patient})

@user_passes_test(auth_permission.is_nurse)
def add_new_opd_visit(request):
    if request.method == 'POST':
        form = PatientOPDVisitsWithClinicIDForm(request.POST)
        if form.is_valid():
            patient_id = form.cleaned_data['patient_id']
            patient = Patient.objects.get(patient_clinic_id=patient_id)
            opd_visit = form.save(commit=False)
            opd_visit.patient = patient
            opd_visit.save()
            messages.success(request, 'Patient vitals added successfully')
            form = PatientOPDVisitsWithClinicIDForm()
        else:
            messages.error(request, 'Form submission failed. Please correct the errors below.')

    else:
        form = PatientOPDVisitsWithClinicIDForm()

    return render(request,'opd/opd_visit_record.html',{'form':form})

@user_passes_test(auth_permission.is_nurse)
def opd_visits_record(request):
    opd_visits = PatientOPDVisit.objects.all()
    return render(request,'opd/opd_visits_list.html',{'opd_visits':opd_visits})

@user_passes_test(auth_permission.is_nurse)
def edit_opd_visit_record(request, patient_id):
    try:
        opd_visit = PatientOPDVisit.objects.get(pk=patient_id)
    except PatientOPDVisit.DoesNotExist:
        messages.error(request,'OPD visit record does not exist')
        return redirect('opd_visit_list')

    if request.method == 'POST':
        form = PatientOPDVisitsWithClinicIDForm(request.POST, instance=opd_visit)
        if form.is_valid():
            form.save()
            messages.success(request,f'OPD Visit Record successfully Updated')
            return redirect('opd_visit_list')
        else:
            messages.error(request, 'Form submission failed. Please correct the errors below.')
    else:
        form = PatientOPDVisitsWithClinicIDForm(instance=opd_visit)

    return render(request, 'opd/edit_opd_visit_record.html', {'form': form, 'patient': opd_visit})
@csrf_exempt
def check_patient_existence(request,patient_id):
    patient_exists = Patient.objects.filter(patient_clinic_id=patient_id).exists()
    response_data = {'exists': patient_exists}

    return JsonResponse(response_data)

class PatientListView(ListView):
    model = Patient
    template_name = 'opd/opd_patients_records.html'  # Create this template
    context_object_name = 'patients'

@user_passes_test(auth_permission.is_record_manager_or_hospital_registrar)
@csrf_exempt
def fetch_patient_by_id(request, patient_id):
    try:
        patient = Patient.objects.get(id=patient_id)
        # patient_data = serializers.serialize('json', [patient], cls=DjangoJSONEncoder)
        # # Serialize the patient data to JSON
        patient_data = {
            'Patient ID': patient.patient_clinic_id,
            'First Name': patient.first_name,
            'Last Name': patient.last_name,
            'Phone Number': patient.phone_number,
            'Email': patient.email,
            'Sex': patient.sex,
            'Age': patient.age,
            'Marital Status': patient.marital_status,
            'Religion': patient.religion,
            'Tribe':patient.tribe,
            'Patient Type': patient.patient_type,
            'Race': patient.race,
            'Date of Birth': patient.date_of_birth,
            'Place of Birth': patient.place_of_birth,
            'Index/Staff ID': patient.index_or_staff_id,
            'Occupation': patient.occupation,
            'Residential Address':patient.residential_address,
            'Business Address' : patient.business_address,
            'Next of Kin' : patient.next_of_kin,
            'Phone number of Next of Kin':patient.phone_number_of_next_of_kin,
            'Address Of Next of Kin': patient.address_next_of_kin,
            'Date Registered': patient.created,
            'Last Modified': patient.modified,

        }

        return JsonResponse({'patient': patient_data})
    except Patient.DoesNotExist:
        return JsonResponse({'error': 'Patient not found'}, status=404)
@user_passes_test(auth_permission.is_record_manager)
def search_patients(request):
    if request.method == 'GET':
        search_term = request.GET.get('search-term', '')
        patients = Patient.objects.filter(
            Q(patient_clinic_id__contains=search_term) |
            Q(first_name__icontains=search_term) |
            Q(last_name__icontains=search_term) |
            Q(index_or_staff_id__icontains=search_term) |
            Q(phone_number__icontains=search_term)
        )
        return render(request, 'opd/opd_patients_records.html', {'patients': patients, 'search_term': search_term})




