from django.conf.urls import url, include

from rest_framework import routers

from api.views import user

routers = routers.DefaultRouter()

routers.register(r'project', user.UserViewSet)



urlpatterns = [

    url(r'^', include(routers.urls)),

]

