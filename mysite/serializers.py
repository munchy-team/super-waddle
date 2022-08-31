from rest_framework import serializers, status
from progress.models import Users
from django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('userId', 'firstName', 'lastName', 'email')