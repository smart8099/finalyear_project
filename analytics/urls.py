from django.urls import path
from .views import admin_home,opd_analysis,register_new_user,admin_opd_visits_record,patient_list,show_admin_profile,delete_patient_record,delete_patient_opd_visit_record,search_patients,opd_visit_search

urlpatterns = [
    path('', admin_home, name='admin_index'),
    path('opd_analysis',opd_analysis,name='opd_analysis'),
    path('register',register_new_user,name='admin_register'),
    path('opd_visits_records',admin_opd_visits_record,name='admin_opd_visits_record'),
    path('list_patients',patient_list, name='list_patients'),
    path('show_admin_profile',show_admin_profile,name='show_admin_profile'),
    path('delete_patient/<int:patient_id>',delete_patient_record,name='delete_patient'),
    path('delete_opd_visit_record/<int:visit_id>',delete_patient_opd_visit_record,name='delete_opd_visit'),
    path('admin_search_patient',search_patients,name='admin_search_patient'),
    path('opd_visit_search',opd_visit_search,name='admin_search_opd_visit')
   ]

    #  path('patient/<int:patient_id>/', patient_view, name='patient'),


