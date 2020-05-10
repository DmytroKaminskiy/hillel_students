from django.contrib import admin
from django.conf import settings
# from students_tracker import settings  WRONG

from django.urls import include, path

from students import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('students/', include('students.urls')),

    path('', views.index, name='index'),

    # TODO remove
    path('hello-world/', views.hello_world),
    path('teacher/create/', views.create_student, name='teacher-create'),  # /teachers/create/

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
