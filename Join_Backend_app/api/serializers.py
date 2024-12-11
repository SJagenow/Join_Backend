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
    contacts = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), many=True)
    contacts_details = serializers.SerializerMethodField()

    class Meta:
        model = Tasks
        fields = ['id', 'title', 'description', 'contacts', 'contacts_details', 'dueDate', 'priority', 'category', 'label', 'subtasks']

    def get_contacts_details(self, obj):
        return [{"id": contact.id, "name": contact.name or "No name"} for contact in obj.contacts.all()]

    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        contacts = validated_data.pop('contacts', [])
        task = Tasks.objects.create(**validated_data)

        for subtask_data in subtasks_data:
            Subtask.objects.create(task=task, **subtask_data)

        task.contacts.set(contacts)
        return task

    def update(self, instance, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        contacts = validated_data.pop('contacts', [])

        # Update task fields
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.dueDate = validated_data.get('dueDate', instance.dueDate)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.label = validated_data.get('label', instance.label)
        instance.category = validated_data.get('category', instance.category)
        instance.save()

        # Update subtasks
        existing_subtasks = {subtask.id: subtask for subtask in instance.subtasks.all()}
        new_subtasks = []

        for subtask_data in subtasks_data:
            subtask_id = subtask_data.get('id')
            if subtask_id and subtask_id in existing_subtasks:
                # Update existing subtask
                subtask = existing_subtasks.pop(subtask_id)
                subtask.title = subtask_data.get('title', subtask.title)
                subtask.done = subtask_data.get('done', subtask.done)
                subtask.save()
            else:
                # Add new subtask
                new_subtasks.append(Subtask(task=instance, **subtask_data))

        # Delete removed subtasks
        for subtask in existing_subtasks.values():
            subtask.delete()

        # Bulk create new subtasks
        Subtask.objects.bulk_create(new_subtasks)

        # Update contacts
        instance.contacts.set(contacts)
        return instance

 


        