from django.conf.urls import url, include

from rest_framework import routers

from .views.user import UserView
from .views.profile import ProfileView

routers = routers.DefaultRouter()


urlpatterns = [

    url(r'^profiles$', ProfileView.as_view()),

    # Users
    url(r'^users$', UserView.as_view()),
]

