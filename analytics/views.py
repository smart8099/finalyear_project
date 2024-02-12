from django.shortcuts import render, redirect
from users.forms import CustomUserCreationForm
from django.contrib import messages
from opd.models import PatientOPDVisit
from django.views.generic import ListView
from opd.models import Patient
from hyperX_core.utils import auth_permission
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseNotAllowed,HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
# Create your views here.

@user_passes_test(auth_permission.is_hyperx_admin)
def admin_home(request):
    return render(request, 'analytics/index.html')


@user_passes_test(auth_permission.is_hyperx_admin)
def opd_analysis(request):
    return render(request, 'analytics/opd_analysis.html')





@user_passes_test(auth_permission.is_hyperx_admin)
def register_new_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account successfully created')
            # Additional processing if needed
            return redirect('login')  # Redirect to login page after successful registration
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'analytics/register.html', {'form': form})


@user_passes_test(auth_permission.is_hyperx_admin)
def admin_opd_visits_record(request):
    opd_visits = PatientOPDVisit.objects.all()
    return render(request, 'analytics/opd_analysis.html', {'opd_visits': opd_visits})


@user_passes_test(auth_permission.is_hyperx_admin)
def patient_list(request):
    patients = Patient.objects.all()
    count = len(patients)
    context = {'patients': patients,'patient_count':count}
    return render(request, 'analytics/patient_data.html', context)


@user_passes_test(auth_permission.is_hyperx_admin)
def show_admin_profile(request):
    # incoming_patients = LabRequest.objects.filter(status='Lab Requested').select_related('patient')
    full_name = f"{request.user.first_name} {request.user.last_name}"
    return render(request,'analytics/profile.html',{'full_name':full_name})


@user_passes_test(auth_permission.is_hyperx_admin)
def delete_patient_record(request,patient_id):
    print(f'patient id requested, {patient_id}')
    patient = get_object_or_404(Patient, id=patient_id)
    print(f'patient is {patient}')

    if request.method == 'POST':
        # Perform the delete operation here
        patient.delete()
        # Redirect to the desired URL
        return HttpResponseRedirect(reverse('list_patients'))  # Replace 'desired_url_name' with your URL pattern name
    return HttpResponseNotAllowed(['POST'])


@user_passes_test(auth_permission.is_hyperx_admin)
def delete_patient_opd_visit_record(request,visit_id):
    visit_record = get_object_or_404(PatientOPDVisit, id=visit_id)
    print(visit_record)

    if request.method == 'POST':
        # Perform the delete operation here
        visit_record.delete()
        # Redirect to the desired URL
        return HttpResponseRedirect(reverse('admin_opd_visits_record'))  # Replace 'desired_url_name' with your URL pattern name
    return HttpResponseNotAllowed(['POST'])

@user_passes_test(auth_permission.is_hyperx_admin)
def search_patients(request):
    patient_count = Patient.objects.count()
    if request.method == 'GET':
        search_term = request.GET.get('search-term', '')
        patients = Patient.objects.filter(
            Q(patient_clinic_id__contains=search_term) |
            Q(first_name__icontains=search_term) |
            Q(last_name__icontains=search_term) |
            Q(index_or_staff_id__icontains=search_term) |
            Q(phone_number__icontains=search_term)
        )
        return render(request, 'analytics/patient_data.html', {'patients': patients, 'search_term': search_term,'patient_count':patient_count})



@user_passes_test(auth_permission.is_hyperx_admin)
def opd_visit_search(request):
    # patient_count = Patient.objects.count()
    if request.method == 'GET':
        search_term = request.GET.get('search-term', '')

        patients = PatientOPDVisit.objects.filter(
            Q(patient_id=search_term) |
            Q(temperature__icontains=search_term)|
            Q(pulse_rate__icontains=search_term) |
            Q(blood_pressure__icontains=search_term) |
            Q(weight__icontains=search_term)
        )

        return render(request, 'analytics/opd_analysis.html', {'opd_visits': patients, 'search_term': search_term})