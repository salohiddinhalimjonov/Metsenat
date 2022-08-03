from rest_framework import serializers
from student.models.otm import OTM


class OTMSerializer(serializers.ModelSerializer):
    class Meta:
        model = OTM
        fields = [
            'id',
            'name'
        ]