from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import mixins,generics,viewsets
from rest_framework import status
from Join_Backend_app.api.serializers import ProfileSerializer, TaskSerializer
from Join_Backend_app.models import Profile , Tasks


class ProfileView(generics.ListCreateAPIView):
   
   queryset = Profile.objects.all()
   serializer_class = ProfileSerializer


class ProfileSingleView(generics.RetrieveUpdateDestroyAPIView):
   
   queryset = Profile.objects.all()
   serializer_class = ProfileSerializer
 
class TaskView(generics.ListCreateAPIView):
   
   queryset = Tasks.objects.all()
   serializer_class = TaskSerializer

class TaskSingleView(generics.RetrieveUpdateDestroyAPIView):

   queryset = Tasks.objects.all()
   serializer_class = TaskSerializer