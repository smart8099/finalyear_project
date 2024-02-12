from django.shortcuts import render,redirect
from opd.models import PatientOPDVisit,Patient
from django.views.decorators.csrf import csrf_exempt
from .forms import  PhysicianDiagnosticForm
from django.contrib import messages
from lab.models import LabTestsAvailable
from django.views.decorators.http import require_POST
import json
from django.http import JsonResponse
from lab.models import LabRequest, LabTestResult
def physician_homepage(request):
    incoming_patients = PatientOPDVisit.objects.filter(status='Pending OPD').select_related('patient')

    return render(request,'physician/physician_base.html',{'incoming_patients':incoming_patients})


def diagnosis_view(request, patient_id):
    # Fetch patient-specific data as needed
    # Render the patient-specific HTML page
    patient_visit = PatientOPDVisit.objects.get(patient_id=patient_id, status='Pending OPD')
    incoming_patients = PatientOPDVisit.objects.filter(status='Pending OPD').select_related('patient')
    # performed_tests = LabTestResult.objects.get()
    lab_tests = LabTestsAvailable.objects.all()
    if request.method == 'POST':
        form = PhysicianDiagnosticForm(request.POST)

        if form.is_valid():
            diagnostic = form.save(commit=False)
            diagnostic.patient = patient_visit.patient
            diagnostic.opd_visit = patient_visit
            diagnostic.save()
            messages.success(request,f'Diagnostic Record successfully Updated')
            PatientOPDVisit.objects.filter(id=patient_visit.id).update(status='Seen Physician')
            form = PhysicianDiagnosticForm()
            redirect('physician_index')
        else:
            messages.error(request, 'Form submission failed. Please correct the errors below.')

    else:
        form = PhysicianDiagnosticForm()



    return render(request, 'physician/physician_diagnostic.html',{'patient_visit':patient_visit,'incoming_patients':incoming_patients,'form':form,'lab_tests': lab_tests})


@require_POST
def request_lab_tests(request):
    # Get the selected lab test IDs from the POST data
    selected_lab_tests_json = request.POST.get('selected_lab_tests')
    selected_lab_test_ids = json.loads(selected_lab_tests_json)
    patient_id = request.POST.get('patient_visit_id')

    patient = Patient.objects.get(id=patient_id)
    opd_visit = PatientOPDVisit.objects.get(patient=patient,status='Pending OPD')

    lab_request = LabRequest(patient_id=patient_id,opd_visit_id=opd_visit.id)
    lab_request.save()

    lab_tests = LabTestsAvailable.objects.filter(id__in=selected_lab_test_ids)
    lab_request.lab_tests.add(*lab_tests)


    response_data = {'message': 'Lab tests submitted successfully'}

    return JsonResponse(response_data)


def show_profile(request):
    full_name = f"{request.user.first_name} {request.user.last_name}"
    return render(request,'physician/profile.html',{'full_name':full_name})