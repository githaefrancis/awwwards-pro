from django.urls import re_path
from . import views
urlpatterns = [
    re_path('^profile/$',views.ProfileDetails.as_view()),
    re_path('^projects/$',views.ProjectList.as_view())
]
