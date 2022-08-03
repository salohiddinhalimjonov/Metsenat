from rest_framework.viewsets import ModelViewSet
from student.models.otm import OTM
from student.serializers.otm import OTMSerializer


class OTMViewSet(ModelViewSet):
    serializer_class = OTMSerializer

    def get_queryset(self):
        return OTM.objects.all()
