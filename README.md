0. Добавить поле phone в модель Student
(2) 1. Сделать raise ошибки если в поле phone ввели не цифры. (StudentCreateForm) django raise error in form
(2) 2. Student, Teacher поля first_name and last_name сделать str.capitalize(). Добавить в сигнал (pre_save). Создать дата миграцию.
(4) 3. Создать мидлварь LogMiddleware которая будет записывать параметры request.path, request.method, execution_time (diff),
   если запрос был на админку (/admin/)
(1) 4. https://github.com/jazzband/django-silk
(1) 5. Теория


class Logger(models.Model):
    method = models.CharField
    path = ...
    execution_time = ...
    created = DateTimeField (when object was created) auto_now_add???

https://docs.djangoproject.com/en/2.2/topics/http/middleware/#middleware 

https://simpleisbetterthancomplex.com/tutorial/2016/07/28/how-to-create-django-signals.html
before save
instance.save()
after save
