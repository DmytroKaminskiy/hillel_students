from django.urls import path

from students import views

app_name = 'students'

urlpatterns = [
    path('list/', views.students, name='list'),  # reverse('students:students-list')
    path('create/', views.create_student, name='create'),
    path('edit/<int:pk>/', views.edit_student, name='edit'),  # /studets/edit/25/
    path('delete/<int:pk>/', views.delete_student, name='delete'),
    path('slow/', views.slow, name='slow'),
]
