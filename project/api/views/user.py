from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.user import UserSerializer

User = get_user_model()


class UserView(APIView):
    @staticmethod
    def get(request):
        """
        List users
        """

        users = User.objects.all()
        return Response(UserSerializer(users, many=True).data)