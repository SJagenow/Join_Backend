from rest_framework import serializers
from Join_Backend_app.models import Profile,Tasks,Subtask


class ProfileSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Profile
        fields = '__all__'

class SubtaskSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Subtask
        fields = '__all__'
        

class TaskSerializer(serializers.ModelSerializer):


   class Meta:
        model = Tasks
        fields = '__all__'




        