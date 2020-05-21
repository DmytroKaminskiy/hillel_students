import random
import string

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from students.models import Student, Group
from students.forms import StudentCreateForm
from students.tasks import slow_func, print_student


def generate_student(request):
    Student.objects.create(age=...)
    return HttpResponse()


def generate_password(length: int = 10) -> str:
    choices = string.ascii_letters + string.digits + string.punctuation

    password = ''
    for _ in range(length):
        password += random.choice(choices)

    return password


def hello_world(request):  # from flask import request
    return HttpResponse(
        generate_password(
            int(request.GET['length'])
        )
    )


def students(request):

    # parse parameters
    params = [
        'age',
        'age__gt',
        'first_name',
        'first_name__startswith',
        'last_name',
        'id',
    ]

    students_queryset = Student.objects.all()  # SELECT * FROM students_student;

    for param in params:
        value = request.GET.get(param)
        if value:
            students_queryset = students_queryset.filter(**{param: value})  # age=29, last_name=Dima

    return render(request, 'students-list.html', context={'students': students_queryset})


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def create_student(request):
    '''
    GET
    
    HEAD
    /create/?first_name=Name&last_name=LNAme
    BODY
    ..........

    POST
    HEAD
    /create/
    BODY
    first_name=Name&last_name=LNAme

    URLS ( /create/ ) -> view (def create_student)
    
    CRUD - 
    C - create POST
    R - read GET
    U - update PUT, PATCH
    D - delete DELETE

    OPTIONS - all available methods
    '''

    if request.method == 'POST':
        form = StudentCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    elif request.method == 'GET':
        form = StudentCreateForm()

    context = {'create_form': form}

    return render(request, 'create.html', context=context)


@csrf_exempt
def edit_student(request, pk):
    # ? id
    # student_id = request.GET.get('student_id')
    # print('STUDENT ID:', pk)
    # from django.http import HttpResponse, HttpResponseRedirect, Http404

    # try:
    #     student = Student.objects.get(id=pk)
    # except Student.DoesNotExist:
    #     raise Http404
    student = get_object_or_404(Student, id=pk)

    if request.method == 'POST':
        form = StudentCreateForm(request.POST, instance=student)

        if form.is_valid():  # form.clean()
            form.save()  #
            return HttpResponseRedirect(reverse('students:list'))

    elif request.method == 'GET':
        form = StudentCreateForm(instance=student)

    context = {'form': form, 'instance': student}

    return render(request, 'edit.html', context=context)


def delete_student(request, pk):
    print(pk)
    print('delete_student')
    return HttpResponse(f'ID: {pk}')


def slow(request):
    from random import randint
    n = randint(1, 10)

    # slow_func.delay(n)  # 1
    # slow_func.apply_async(args=[n], countdown=10)  # 2
    slow_func.apply_async(kwargs={'num': n}, countdown=10)  # 2

    student = Student.objects.first()
    # int, float, str, list, dict, bool
    print_student.apply_async(args=[student.id], countdown=20)

    return HttpResponse('SLOW')


def groups(request):
    objects = Group.objects.all().select_related('head')
    return render(request, 'groups.html',
                  context={'objects_list': objects})
