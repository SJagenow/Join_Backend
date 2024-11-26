from rest_framework import serializers
from Join_Backend_app.models import Profile,Tasks,Subtask


class ProfileSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Profile
        fields = '__all__'


        

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['title', 'done']

class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, required=False) 

    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', 'contacts', 'dueDate', 'priority', 'category', 'label', 'subtasks']

    def create(self, validated_data):
       
        subtasks_data = validated_data.pop('subtasks', [])
        
      
        task = Tasks.objects.create(**validated_data)
        
       
        for subtask_data in subtasks_data:
            Subtask.objects.create(task=task, **subtask_data)
        
        return task


        