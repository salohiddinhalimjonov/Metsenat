from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.response import Response


class LogoutView(APIView):

    def post(self, request):
        user = request.user
        token = get_object_or_404(Token, user=user)
        token.delete()
        return Response(status=status.HTTP_205_RESET_CONTENT)
