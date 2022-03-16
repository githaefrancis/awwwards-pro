from django.urls import re_path
from . import views
urlpatterns = [
    re_path('^profiles/$',views.ProfileDetails.as_view())
]
