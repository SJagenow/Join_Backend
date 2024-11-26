from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import mixins,generics,viewsets
from rest_framework import status
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
    contactId = self.kwargs.get('contactId')
    try:
        return get_object_or_404(Profile, id=contactId)
    except Http404:
        print(f"Kein Kontakt mit der ID {contactId} gefunden.")
        raise

 
class TaskView(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
     
        task = serializer.save()

      
        subtasks_data = self.request.data.get('subtasks', [])
        for subtask_data in subtasks_data:
        
            Subtask.objects.create(task=task, **subtask_data)



class TaskSingleView(generics.RetrieveUpdateDestroyAPIView):

   queryset = Tasks.objects.all()
   serializer_class = TaskSerializer


class SubtaskView(generics.ListCreateAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer



class SubtaskSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer
