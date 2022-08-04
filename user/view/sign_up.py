from rest_framework import permissions
from rest_framework.views import APIView
from user.models import User
from user.serializers.user import SignUpSerializer
from user.services.sign_up import sign_up


class SignUpView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return sign_up(**serializer.validated_data)
