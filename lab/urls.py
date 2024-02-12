from django.urls import path
from .views import lab_homepage,lab_results_view,submit_lab_results,show_lab_profile

urlpatterns = [
    path('',lab_homepage,name='lab_index'),
    path('lab_results/<int:lab_request_id>/', lab_results_view, name='lab_results'),
    path('submit_lab',submit_lab_results,name='submit_lab_results'),
    path('profile',show_lab_profile,name='show_lab_profile')



    ]

