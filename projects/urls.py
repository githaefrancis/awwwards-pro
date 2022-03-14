from . import views
from django.urls import path,re_path


urlpatterns=[

path('',views.index,name='home'),
path('project/new',views.new_project,name='create_project'),
re_path('^project/(\d+)$',views.single_project,name='view_project'),
re_path('^project/(\d+)/vote$',views.vote,name='vote'),

]