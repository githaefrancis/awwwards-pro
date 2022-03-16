from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from projects.models import UserProfile,Project
from .serializer import UserProfileSerializer,ProjectSerializer
from api import serializer

class ProfileDetails(APIView):
  '''
  API endpoint to fetch user profiles and individual projects.
  '''
  def get(self,request,format=None):
    all_profiles=UserProfile.objects.all()
    serializers=UserProfileSerializer(all_profiles,many=True)
    return Response(serializers.data)


class ProjectList(APIView):
  '''
  API endpoint to fetch all projects posted to the site
  '''
  def get(self,request,format=None):
    all_projects=Project.get_all_projects()
    serializers=ProjectSerializer(all_projects,many=True)
    return Response(serializers.data)
    