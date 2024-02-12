from django.urls import path
from .views import physician_homepage, diagnosis_view,request_lab_tests,show_profile

urlpatterns = [
    path('', physician_homepage, name='physician_index'),
    path('diagnosis/<int:patient_id>/', diagnosis_view, name='diagnosis'),
    path('lab_request/',request_lab_tests,name='request_lab_tests'),
    path('profile',show_profile,name='show_profile')

    #  path('patient/<int:patient_id>/', patient_view, name='patient'),

]
