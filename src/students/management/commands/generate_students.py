import random

from django.core.management.base import BaseCommand

from faker import Faker

from students.models import Student


class Command(BaseCommand):
    help = 'Generate random students'  # noqa  help is python builtins but django command requires it.

    def handle(self, *args, **options):
        fake = Faker()

        # Model

        # objects.bulk_create

        students = []
        for _ in range(1000):
            students.append(Student(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                age=random.randint(10, 100),
            ))

        Student.objects.bulk_create(students)

        # Student.objects.bulk_create([student])

        # for _ in range(1000):
        #     Student.objects.create(
        #         first_name=fake.first_name(),
        #         last_name=fake.last_name(),
        #         age=random.randint(10, 100),
        #     )
