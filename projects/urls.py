from . import views
from django.urls import path


urlpatterns=[

path('',views.index,name='home'),
path('project/new',views.new_project,name='create_project'),

]