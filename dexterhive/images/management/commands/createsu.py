import os

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username="adminDH18").exists():
            User.objects.create_superuser("adminDH18", "sheeraz@dexterhive", "yiad1n3q71PQ9n8V7aGmlf266Id1fTaT")