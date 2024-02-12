from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from lab.models import LabRequest
from .models import LabTestResult
from django.shortcuts import redirect
from opd.models import PatientOPDVisit
# Create your views here.
def lab_homepage(request):
    incoming_patients = LabRequest.objects.filter(status='Lab Requested').select_related('patient')
    print(incoming_patients)
    return render(request,'lab/lab_base.html',{'incoming_patients':incoming_patients})

# def lab_tests_view(request, patient_id):
#     # Fetch patient-specific data as needed
#     # Render the patient-specific HTML page
#     incoming_patients = LabRequest.objects.filter(status='Lab Requested').select_related('patient')
#     lab_tests = LabTestsAvailable.objects.all()
#     if request.method == 'POST':
#         form = PhysicianDiagnosticForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             messages.success(request,f'Diagnostic Record successfully Updated')
#             form = PhysicianDiagnosticForm()
#         else:
#             messages.error(request, 'Form submission failed. Please correct the errors below.')
#
#     else:
#         form = PhysicianDiagnosticForm()
#
#
#
#     return render(request, 'lab/patient_lab.html')

def lab_results_view(request, lab_request_id):
    incoming_patients = LabRequest.objects.filter(status='Lab Requested').select_related('patient')
    lab_request = get_object_or_404(LabRequest, id=lab_request_id)
    selected_lab_tests = lab_request.lab_tests.all()
    context = {'lab_request': lab_request, 'selected_lab_tests': selected_lab_tests,'incoming_patients':incoming_patients}

    return render(request, 'lab/patient_lab.html', context)


def submit_lab_results(request):
    if request.method == 'POST':
        # Assuming you have a way to identify the lab request, e.g., through a lab_request_id
        lab_request_id = request.POST.get('lab_request_id')
        opd_visit_id = request.POST.get('opd_visit_id')
        lab_request = LabRequest.objects.get(id=lab_request_id)
        selected_lab_tests = lab_request.lab_tests.all()
        opd_visit = PatientOPDVisit.objects.get(id=opd_visit_id)


        for lab_test in selected_lab_tests:
            lab_test_result_key = f'lab_test_results_{lab_test.id}'
            lab_test_result_value = request.POST.get(lab_test_result_key)
            print(lab_test_result_value)

            # Create a LabTestResult object and associate it with the lab request
            lab_test_result = LabTestResult(
                opd_visit=opd_visit,
                lab_request=lab_request,
                lab_test=lab_test,
                result_value=lab_test_result_value
            )
            lab_test_result.save()

        messages.success(request, 'Lab Result Submitted Successfully')
        LabRequest.objects.filter(id=lab_request_id).update(status='Lab Completed')
        return redirect('lab_index')

    # Handle GET requests or any other logic you need
    return render(request, 'lab/lab_base.html')


def show_lab_profile(request):
    incoming_patients = LabRequest.objects.filter(status='Lab Requested').select_related('patient')
    full_name = f"{request.user.first_name} {request.user.last_name}"
    return render(request,'lab/profile.html',{'full_name':full_name,'incoming_patients':incoming_patients})