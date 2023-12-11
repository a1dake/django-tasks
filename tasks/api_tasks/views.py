from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from .utils import pagination_and_filtering


@api_view(['POST', 'GET'])
def tasks_view(request):
    """
    List and Create Tasks
    """

    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        tasks = Task.objects.all()
        tasks, paginator = pagination_and_filtering(request, tasks)

        serializer = TaskSerializer(tasks, many=True)
        return paginator.get_paginated_response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def task_detail_view(request, task_id: int):
    """
    Retrieve, Update, and Delete Task
    """

    task = get_object_or_404(Task, pk=task_id)

    if task:
        if request.method == 'GET':
            serializer = TaskSerializer(task)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)