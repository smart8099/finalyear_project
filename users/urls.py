from django.urls import path
from .views import registerpage,loginpage,CustomLogoutView

urlpatterns = [
    path('login/',loginpage, name='login'),
    path('logout/',CustomLogoutView.as_view(), name='logout'),
    path('register/', registerpage, name='register'),
]
