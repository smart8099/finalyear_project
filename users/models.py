from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group, PermissionsMixin
from django.db import models



class UserManager(BaseUserManager):
    def create_user(self, username, first_name, last_name, email, phone_number, user_type, password=None):
        """
        Create and save a regular user with the given details.
        """
        if not first_name:
            raise ValueError("User should have a first name")

        if not last_name:
            raise ValueError("User should have a last name")

        if not username:
            raise ValueError("The username field is required.")

        if not email:
            raise ValueError("User should have an email")

        if not phone_number:
            raise ValueError("User should have a phone number")

        if not user_type:
            raise ValueError("User should have a user type")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
            phone_number=phone_number,
            user_type=user_type,
        )
        user.set_password(password)  # Hash the password
        user.save(using=self._db)

        # Assign user to appropriate group based on user_type
        group_name = user_type  # Create group name from user_type
        group, _ = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)
        return user

    def create_superuser(self, username, first_name, last_name, email, user_type,phone_number,  password=None):
        if password is None:
            raise ValueError("Password cannot be None")

        if user_type not in ["ADMIN", "HOSPITAL_REGISTRAR", "CLINIC_SUPERVISOR"]:
            raise ValueError("Invalid user type for creating a superuser")

        if not phone_number:
            raise ValueError("Phone number is needed")

        user = self.create_user(username, first_name, last_name, email,phone_number, user_type, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        ("HOSPITAL_REGISTRAR", "HOSPITAL_REGISTRAR"),
        ("NURSE", "NURSE"),
        ("LAB_TECHNICIAN", "LAB_TECHNICIAN"),
        ("PHARMACIST", "PHARMACIST"),
        ("PHYSICIAN", "PHYSICIAN"),
        ("RECORD_MANAGER", "RECORD_MANAGER"),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, db_index=True, unique=True)
    email = models.CharField(max_length=255, unique=True, db_index=True)
    phone_number = models.CharField(max_length=15, unique=True, default="")
    user_type = models.CharField(max_length=255, choices=USER_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name", "email", "user_type","phone_number"]

    objects = UserManager()

    def __str__(self) -> str:
        return f"self.email (self.username)"

