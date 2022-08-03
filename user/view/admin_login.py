from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from user.serializers.admin_login import AdminLoginSerializer
from user.services.admin_login import admin_login


class AdminLoginView(APIView):
    serializer_class = AdminLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return admin_login(**serializer.validated_data)
