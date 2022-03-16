from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from projects.models import UserProfile
from .serializer import UserProfileSerializer

class ProfileDetails(APIView):
  '''
  Api endpoint to fetch user profiles.
  '''
  def get(self,request,format=None):
    all_profiles=UserProfile.objects.all()
    serializers=UserProfileSerializer(all_profiles,many=True)
    return Response(serializers.data)
