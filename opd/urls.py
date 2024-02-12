from django.urls import path
from .views import opd_homepage,add_new_patient,add_new_opd_visit,check_patient_existence,PatientListView,fetch_patient_by_id,search_patients, record_manager_homepage,edit_patient,opd_visits_record,edit_opd_visit_record

urlpatterns = [
    path('',opd_homepage,name='opd_index'),
    path('add_patient',add_new_patient, name='add_patient'),
    path('add_opd_visit',add_new_opd_visit, name='add_opd_visit'),
    path('check_patient_existence/<str:patient_id>/',check_patient_existence, name='check_patient_existence'),
    path('patients_list/', PatientListView.as_view(), name='patient_list'),
    path('fetch_patient_data/<str:patient_id>/', fetch_patient_by_id, name='fetch_patient_data'),
    path('search/', search_patients, name='search_patients'),
    path('record',record_manager_homepage,name='record_manager_index'),
    path('edit_patient/<int:patient_id>/',edit_patient, name='edit_patient'),
    path('edit_opd_visit/<int:patient_id>/', edit_opd_visit_record, name='edit_opd_visit'),
    path('opd_visits',opd_visits_record,name='opd_visit_list')
]
