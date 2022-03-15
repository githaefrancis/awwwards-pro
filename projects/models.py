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

  @classmethod
  def get_project_by_id(cls,id):
    return cls.objects.filter(pk=id).first()


  @classmethod
  def get_all_projects(cls):
    return cls.objects.all()
  
class Rating(models.Model):
  user=models.ForeignKey(User,related_name='rating',on_delete=models.CASCADE)
  project=models.ForeignKey(Project,related_name='rating',on_delete=models.CASCADE)
  design_rating=models.IntegerField()
  usability_rating=models.IntegerField()
  content_rating=models.IntegerField()
  created_at=models.DateTimeField(auto_now_add=True)

  @classmethod
  def check_if_user_has_rated(cls,user,project_id):
    
    project=Project.get_project_by_id(project_id)
    return cls.objects.filter(user=user,project=project)

  def save_rating(self):
    self.save()
  @classmethod
  def get_average_rating(cls,project_id):
    target_project=Project.objects.filter(id=project_id).first()
    all_ratings=Rating.objects.filter(project=target_project).all()
  
    design_average=sum(rating.design_rating for rating in all_ratings)/len(all_ratings)
    usability_average=sum(rating.usability_rating for rating in all_ratings)/len(all_ratings)
    content_average=sum(rating.content_rating for rating in all_ratings)/len(all_ratings)
    return {'design':round(design_average,1),'usability':round(usability_average,1),'content':round(content_average,1)}
