from rest_framework import serializers


class StatisticsSerializer(serializers.Serializer):
    date = serializers.DateField()
