from django.urls import path
from Join_Backend_app.api.views import ProfileSingleView, ProfileView, SubtaskSingleView, SubtaskView, TaskSingleView, TaskView

urlpatterns = [
    path('contacts/', ProfileView.as_view(), name='contact-list'),  # Liste aller Kontakte
    path('contacts/<contactId>/', ProfileSingleView.as_view(), name='contact-detail'),  # Einzelner Kontakt
    path('tasks/', TaskView.as_view(), name='task-list'),  # Liste aller Aufgaben
    path('tasks/<pk>/', TaskSingleView.as_view(), name='task-detail'),  # Einzelne Aufgabe
    path('subtask/', SubtaskView.as_view(), name='subtask-list'),  # Liste der Subtasks
    path('subtask/<pk>/', SubtaskSingleView.as_view(), name='subtask-detail'),  # Einzelner Subtask
]

