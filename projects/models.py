from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class UserProfile(models.Model):
  user=models.ForeignKey(User,related_name='profile',on_delete=models.CASCADE)
  name=models.CharField(max_length=100)
  bio=models.CharField(max_length=500)
  profile_photo=CloudinaryField('image')
  created_at=models.DateTimeField(auto_now_add=True)

  def save_profile(self):
    self.save()


class Project(models.Model):
  user=models.ForeignKey(User,related_name='project',on_delete=models.CASCADE)
  title=models.CharField(max_length=100)
  description=models.CharField(max_length=500)
  url=models.CharField(max_length=500)
  image=CloudinaryField('image')
  created_at=models.DateTimeField(auto_now_add=True)

  def save_project(self):
    self.save()
class Rating(models.Model):
  user=models.ForeignKey(User,related_name='rating',on_delete=models.CASCADE)
  project=models.ForeignKey(Project,related_name='rating',on_delete=models.CASCADE)
  design_rating=models.IntegerField()
  usability_rating=models.IntegerField()
  content_rating=models.IntegerField()
  created_at=models.DateTimeField(auto_now_add=True)

  def save_rating(self):
    self.save()