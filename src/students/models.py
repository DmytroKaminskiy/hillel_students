from django.db import models

# Create your models here.
# ORM - Object relation mapping


class Student(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()  # models.IntegerField
    password = models.CharField(max_length=128, default='')
    phone = models.CharField(max_length=24, default='')

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def info(self) -> str:
        return f'{self.id} {self.first_name} {self.last_name} {self.age}'

    def __str__(self):
        return self.info()

    def save(self, **kwargs):
        print('Before save')
        # self.phone = ''.join(i for i in self.phone if i.isdigit())
        super().save(**kwargs)
        print('After save')


class Group(models.Model):
    name = models.CharField(max_length=64)
    # head = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True)
    head = models.ForeignKey('students.Student',  # head_id
                             on_delete=models.SET_NULL,
                             null=True, related_name='groups')

# OneToOne
# OneToMany
# ManyToMany

