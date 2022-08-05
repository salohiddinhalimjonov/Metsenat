from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from user.models import User


def sign_up(**kwargs):
    username = kwargs.pop('username')
    password = kwargs.pop('password')
    if User.objects.filter(email__iexact=username).exists():
        return Response({'detail': 'email already exists'}, status=status.HTTP_400_BAD_REQUEST)
    user = User(username=username, is_superuser=True, is_staff=True, **kwargs)
    user.set_password(password)
    user.save()
    token = Token.objects.create(user=user)
    return Response({"token": token.key}, status=status.HTTP_201_CREATED)
