from rest_framework import serializers
from projects.models import UserProfile
from django.contrib.auth.models import User



class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model=UserProfile
    fields=('user','name','bio','profile_photo')