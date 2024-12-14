from django.urls import path
from Join_Backend_app.api import views
from Join_Backend_app.api.views import ContactDetailView, ProfileSingleView, ProfileView, SubtaskSingleView, SubtaskView, TaskCountView, TaskSingleView, TaskView

urlpatterns = [
    path('contacts/', ProfileView.as_view(), name='contact-list'), 
    path('contacts/<contactId>/', ProfileSingleView.as_view(), name='contact-detail'),  
    path('contacts/<int:contact_id>/', ContactDetailView.as_view(), name='contact-details'),
    path('tasks/', TaskView.as_view(), name='task-list'), 
    path('tasks/<pk>/', TaskSingleView.as_view(), name='task-detail'), 
    path('task-counts/', TaskCountView.as_view(), name='task-counts'),
    path('subtask/', SubtaskView.as_view(), name='subtask-list'),
    path('subtask/<int:pk>/', SubtaskSingleView.as_view(), name='subtask-detail'),  
]

