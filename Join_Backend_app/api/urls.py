from django.urls import path, include

from Join_Backend_app.api.views import  ProfileSingleView, ProfileView, TaskSingleView, TaskView


urlpatterns = [
 
    path('contacts/', ProfileView.as_view()),
    path('contacts/<pk>/', ProfileSingleView.as_view()),
    path('tasks/',TaskView.as_view()),
    path('tasks/<pk>/',TaskSingleView.as_view()),
]
