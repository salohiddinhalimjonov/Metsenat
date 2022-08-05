from rest_framework.viewsets import GenericViewSet
from rest_framework import permissions
from rest_framework import mixins
from sponsor.serializers.sponsor import *
from sponsor.models.sponsor import Sponsor


class SponsorViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    filterset_fields = ['created_datetime', 'payment_amount', 'sponsor_status']
    search_fields = ['full_name', 'organization', 'payment_amount']

    def get_queryset(self):
        return Sponsor.objects.all()

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = (permissions.AllowAny,)
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        self.serializer_class = NewSponsorSerializer
        return super(SponsorViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer_class = SponsorUpdateSerializer
        return super(SponsorViewSet, self).update(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        self.serializer_class = SponsorListSerializer
        return super(SponsorViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = SponsorProfileSerializer
        return super(SponsorViewSet, self).retrieve(request, *args, **kwargs)
