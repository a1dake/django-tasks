from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer
from rest_framework.pagination import PageNumberPagination


class TaskPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 50

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
    ordering = ['-is_done', 'created_at']