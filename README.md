(4) 1. установить flake8 и модули (flake8, flake8-import-order, flake8-builtins, flake8-print). Почистить код (flake8 ./src)
(2) 2. Добавить проверку flake8 на travis
(2) 3. Написать команду которая будет генерировать 100 случайных учителей (python manage.py generate_teachers) (https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/)
       добавить параметр который регилирует количество созд. учителей. (по умл. 100) (python manage.py generate_teachers 50)
(2) 4. Вывести список учителей с возможностью фильтрации по полям age, first_name, last_name.


# filter, exclude, order_by, count, 
# __ in, lt, lte, gt, gte
# startswith, endswith, istartswith, iendswith, exact, iexact
