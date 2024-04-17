from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Todo
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id']
        
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    # user = UserSerializer()
    # user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'created_at', 'user_attributes', 'timepassed']
