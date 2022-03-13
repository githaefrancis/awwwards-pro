from django.test import TestCase
from django.contrib.auth.models import User 
from .models import Project, Rating, UserProfile
# Create your tests here.
class TestProject(TestCase):
  def setUp(self):
    self.user=User(email='francis@gmail.com',username='fgithae',first_name='user',last_name='fgithae')
    self.project=Project(title='insta',description='insta clone',url='https://insta-mirro.com',image='https://cloudinary.com/insta.jpg',user=self.user)
    self.profile=UserProfile(name='francis githae',bio='a frank effect',user=self.user,profile_photo='photo/photo.jpg')
    self.rating=Rating(user=self.user,project=self.project,design_rating=5,usability_rating=6,content_rating=5)

  def test_instance(self):
    self.assertTrue(isinstance(self.user,User))
    self.assertTrue(isinstance(self.project,Project))


  def test_save_project(self):
    self.user.save()
    self.project.save_project()

    self.assertTrue(len(Project.objects.all())>0)

  def test_save_profile(self):
    self.user.save()
    self.profile.save_profile()
    self.assertTrue(len(UserProfile.objects.all())>0)

  def test_save_rating(self):
    self.user.save()
    self.project.save_project()
    self.rating.save_rating()
    self.assertTrue(len(Rating.objects.all())>0)

