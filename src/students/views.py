import random
import string

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from students.models import Student

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
    '''
    age=53&first_name=Paul&last_name=Schwartz
    '''

    # parse parameters
    params = [
        'age',
        'age__gt',
        'first_name',
        'first_name__startswith',
        'last_name',
        'id',
    ]
    # age = request.GET.get('age')
    # first_name = request.GET.get('first_name')
    # last_name = request.GET.get('last_name')

    students_queryset = Student.objects.all()  # SELECT * FROM students_student;

    for param in params:
        value = request.GET.get(param)
        if value:
            students_queryset = students_queryset.filter(**{param: value})  # age=29, last_name=Dima
            # param == 'age__gt'
            # value == 30
            # .filter(age__gt=30)

    # filter
    # if age:
    #     students_queryset = students_queryset.filter(age=age)
    #
    # if first_name:
    #     students_queryset = students_queryset.filter(first_name=first_name)
    #
    # if last_name:
    #     students_queryset = students_queryset.filter(last_name=last_name)

    # arbeiten!
    response = f'students: {students_queryset.count()}<br/>'

    for student in students_queryset:
        response += student.info() + '<br/>'

    return HttpResponse(response)


def index(request):
    return render(request, 'index.html')



from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_student(request):
    from students.forms import StudentCreateForm

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
            return HttpResponseRedirect('/')

    elif request.method == 'GET':
        form = StudentCreateForm()

    context = {'create_form': form}

    return render(request, 'create.html', context=context)
