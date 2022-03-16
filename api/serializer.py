from dataclasses import fields
from rest_framework import serializers
from projects.models import UserProfile,Project
from django.contrib.auth.models import User


class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model=Project
    fields=['title','description','url','image','created_at']

class UserSerializer(serializers.ModelSerializer):
  project=ProjectSerializer(many=True)
  class Meta:
    model=User
    fields=['username','email','project']


class UserProfileSerializer(serializers.ModelSerializer):
  user=UserSerializer(many=False)
  class Meta:
    model=UserProfile
    fields=('user','name','bio','profile_photo',)