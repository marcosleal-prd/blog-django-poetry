from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


def add_user():
    if not User.objects.filter(is_superuser=True).exists():
        u = User(username="admin")
        u.set_password("test")
        u.is_superuser = True
        u.is_staff = True
        u.save()


def create_user(username=None, password=None, is_super=False):
    username = username if username is not None else "fake-username-test"
    password = password if password is not None else "test"

    if is_super:
        return User.objects.create_superuser(username, None, password)
    else:
        return User.objects.create(username=username, password=password)


class Command(BaseCommand):
    help = "Create a super user"

    def handle(self, *args, **options):
        add_user()
