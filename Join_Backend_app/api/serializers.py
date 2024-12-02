from rest_framework import serializers
from Join_Backend_app.models import Profile,Tasks,Subtask


class ProfileSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Profile
        fields = ['id', 'name', 'mail', 'phone'] 
        

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['title', 'done']

class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, required=False)
    contacts = ProfileSerializer(many=True)  
    contacts_details = serializers.SerializerMethodField()

    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', 'contacts', 'contacts_details', 'dueDate', 'priority', 'category', 'label', 'subtasks']

    def get_contacts_details(self, obj):
        return [{"name": contact.name} for contact in obj.contacts.all()]

    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        contacts_data = validated_data.pop('contacts', [])

        task = Tasks.objects.create(**validated_data)

        for subtask_data in subtasks_data:
            Subtask.objects.create(task=task, **subtask_data)

        task.contacts.set([contact['id'] for contact in contacts_data])  # IDs setzen

        return task








        