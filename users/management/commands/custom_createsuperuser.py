from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        User = get_user_model()
        username = input("Username: ")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        user_type = input("User type: ")
        phone_number = input("Phone number: ")
        password = input("Password: ")

        User.objects.create_superuser(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            user_type=user_type,
            phone_number=phone_number,
            password=password,
        )
        self.stdout.write(self.style.SUCCESS('Superuser created successfully!'))
