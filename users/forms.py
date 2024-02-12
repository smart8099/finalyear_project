from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.conf import settings
from django.contrib.auth.models import Group
class CustomUserCreationForm(forms.ModelForm):
    user_type = forms.ChoiceField(
        choices=User.USER_TYPE_CHOICES,
        widget=forms.RadioSelect,
    )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)


    def save(self, commit=True):
        # Exclude password-related code from UserCreationForm
        DEFAULT_PASSWORD_FOR_NEWLY_REGISTERED_USERS = getattr(settings,"DEFAULT_PASSWORD_FOR_NEWLY_REGISTERED_USERS",'')
        print (f' the default password is {DEFAULT_PASSWORD_FOR_NEWLY_REGISTERED_USERS}')
        user = super().save(commit=False)
        user.user_type = self.cleaned_data["user_type"]
        user_type = self.cleaned_data["user_type"]

        # Set the custom password

        if DEFAULT_PASSWORD_FOR_NEWLY_REGISTERED_USERS:
            user.set_password(DEFAULT_PASSWORD_FOR_NEWLY_REGISTERED_USERS)

        if commit:
            user.save()


        group_name = user_type  # Create group name from user_type
        group, _ = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)

        return user


    class Meta:
        model = User  # Specify your custom user model
        fields = ['first_name', 'last_name','username',  'email', 'phone_number', 'user_type']
