from django.forms import ValidationError
from django.http import Http404, JsonResponse
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
        try:
            return get_object_or_404(Profile, id=contact_id)
        except Http404:
            raise Http404(f"Kontakt mit der ID {contact_id} nicht gefunden.")


class TaskView(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        task_data = self.request.data
        try:
            task = serializer.save() 
            
            subtasks_data = task_data.get('subtasks', [])
            if subtasks_data:
                for subtask_data in subtasks_data:
                    subtask_data['task'] = task.id 
                    subtask_serializer = SubtaskSerializer(data=subtask_data)
                    if subtask_serializer.is_valid():
                        subtask_serializer.save()
                    else:
                        raise ValidationError(f"Invalid subtask data: {subtask_serializer.errors}")
        except ValidationError as e:
            # Fehler bei der Subtask-Erstellung
            return JsonResponse({"error": f"Validation error: {str(e)}"}, status=400)
        except Exception as e:
            # Allgemeiner Fehler
            return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)

        return JsonResponse({"message": "Task created successfully!"}, status=201)

class TaskSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

    def perform_update(self, serializer):
        task = serializer.save() 
        subtasks_data = self.request.data.get('subtasks', [])  
        
        try:
            if subtasks_data:  
                for subtask_data in subtasks_data:
                    Subtask.objects.update_or_create(
                        task=task, 
                        title=subtask_data.get('title'),
                        defaults={'done': subtask_data.get('done')} 
                    )
        except ValidationError as e:
            # Fehler bei der Subtask-Aktualisierung
            return JsonResponse({"error": f"Validation error: {str(e)}"}, status=400)
        except Exception as e:
            # Allgemeiner Fehler
            return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)

        return JsonResponse({"message": "Task updated successfully!"}, status=200)



class SubtaskView(generics.ListCreateAPIView):
    serializer_class = SubtaskSerializer

    def get_queryset(self):
        task_id = self.request.query_params.get('task_id')
        if task_id:
            try:
                return Subtask.objects.filter(task_id=task_id)
            except Exception as e:
                return JsonResponse({"error": f"Failed to fetch subtasks: {str(e)}"}, status=500)
        return Subtask.objects.all()


class SubtaskSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer


class TaskCountView(generics.GenericAPIView, mixins.ListModelMixin):
    def get(self, request, *args, **kwargs):
        count_todo = Tasks.objects.filter(category='todo').count()
        count_done = Tasks.objects.filter(category='done').count()
        count_in_progress = Tasks.objects.filter(category='inprogress').count()
        count_urgent = Tasks.objects.filter(priority='urgent').count()
        count_await = Tasks.objects.filter(category='await').count()

        all_tasks = Tasks.objects.filter(dueDate__isnull=False)
        next_due_date = None

        for task in all_tasks:
            if task.dueDate:
                if not next_due_date or task.dueDate < next_due_date:
                    next_due_date = task.dueDate

        next_due_date_str = next_due_date.strftime('%Y-%m-%d') if next_due_date else 'No upcoming deadlines'

        data = {
            'todo_count': count_todo,
            'done_count': count_done,
            'in_progress_count': count_in_progress,
            'urgent_count': count_urgent,
            'await_count': count_await,
            'next_due_date': next_due_date_str
        }

        return Response(data)


class ContactDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    