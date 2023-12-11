from django.urls import path
from .views import tasks_view, task_detail_view

urlpatterns = [
    path('tasks/', tasks_view, name='tasks_view'),
    path('tasks/<int:task_id>/', task_detail_view, name='task_detail_view'),
]