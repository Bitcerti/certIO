from django.conf.urls import url, include

from rest_framework import routers

from project.api import views


routers = routers.DefaultRouter()

routers.register(r'project', views.UserViewSet)



urlpatterns = [

    url(r'^', include(routers.urls)),

]

