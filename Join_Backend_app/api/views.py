from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import mixins, generics, viewsets
from rest_framework import status
from Join_Backend_app.api import serializers
from Join_Backend_app.api.serializers import ProfileSerializer, SubtaskSerializer, TaskSerializer
from Join_Backend_app.models import Profile, Tasks, Subtask


class ProfileView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        serializer.save()


class ProfileSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        contact_id = self.kwargs.get('contactId')
        return get_object_or_404(Profile, id=contact_id)


class TaskView(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save()  
        subtasks_data = self.request.data.get('subtasks', [])
        
        
        if subtasks_data:
            for subtask_data in subtasks_data:
                subtask_data['task'] = task.id 
                subtask_serializer = SubtaskSerializer(data=subtask_data)
                if subtask_serializer.is_valid():
                    subtask_serializer.save()
                else:
                    raise serializers.ValidationError(f"Invalid subtask data: {subtask_serializer.errors}")




class TaskSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer


class SubtaskView(generics.ListCreateAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer


class SubtaskSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer
