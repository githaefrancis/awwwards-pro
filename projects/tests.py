from django.test import TestCase
from django.contrib.auth.models import User 
from .models import Project
# Create your tests here.
class TestProject(TestCase):
  def setUp(self):
    self.user=User(email='francis@gmail.com',username='fgithae',first_name='user',last_name='fgithae')
    self.project=Project(title='insta',description='insta clone',url='https://insta-mirro.com',image='https://cloudinary.com/insta.jpg',user=self.user)

  def test_instance(self):
    self.assertTrue(isinstance(self.user,User))
    