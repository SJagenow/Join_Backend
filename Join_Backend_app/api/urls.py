from django.urls import path, include

from Join_Backend_app.api.views import  profileView


urlpatterns = [
 
    path('contacts/', profileView.as_view()),
]
