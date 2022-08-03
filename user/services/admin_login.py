from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user.models import User


def admin_login(**kwargs):
    try:
        user = User.objects.get(username=kwargs['username'], is_staff=True)
        if user.check_password(kwargs['password']) is True:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)

        return Response({"detail": "Incorrect password"}, status=status.HTTP_400_BAD_REQUEST)

    except User.DoesNotExist:
        return Response({"detail": "User with the email is not registered or not admin user"},
                        status=status.HTTP_400_BAD_REQUEST)
