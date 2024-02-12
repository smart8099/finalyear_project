from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,LogoutView, PasswordChangeDoneView,PasswordChangeView,PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
# class CustomLoginView(LoginView):
#     template_name = 'registration/login.html'
#
#     def form_valid(self, form):
#         user = form.get_user()
#         print(f'the user is {user}')
#         messages.success(self.request, f'Welcome {user.username}!')
#         return super().form_valid(form)
def loginpage(request):
    if request.method == "POST":
        print(f'the entire request .post is {request.POST}')
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password=password)

        if user is not None:
            auth.login(request,user)
            user = request.user
            if user.user_type == 'NURSE':
                return redirect('opd_index')

            elif user.user_type == 'RECORD_MANAGER':
                return redirect('record_manager_index')

            elif user.user_type == 'PHYSICIAN':
                return redirect('physician_index')
            elif user.user_type == 'LAB_TECHNICIAN':
                return redirect('lab_index')
            elif user.user_type == 'HOSPITAL_REGISTRAR':
                return redirect('admin_index')



            messages.success(request,f'welcome {user.username} ')
            return redirect('/')

        else:

            messages.error(request, f'Incorrect Username/Password ')
            return redirect('/')

    else:
        return render(request,"registration/login.html")

class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        messages.success(request, f"Goodbye, {user.username}")
        return super().dispatch(request, *args, **kwargs)

@login_required
def registerpage(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,f'Account successfully created')
            # Additional processing if needed
            return redirect('login')  # Redirect to login page after successful registration
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def nurse_dashboard(request):
    return render(request, 'opd/opd_nurse.html')