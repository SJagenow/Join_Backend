from rest_framework import serializers
from Join_Backend_app.models import Profile,Tasks


class ProfileSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Profile
        fields = '__all__'