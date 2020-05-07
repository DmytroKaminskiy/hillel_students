from django.contrib import admin
from django.urls import path

from students import views

# cli -> request -> urls.py -> views.py -> response Cli

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index),

    path('hello-world/', views.hello_world),
    path('students/', views.students),
    path('create/', views.create_student), # Ctrl + D
]
