from rest_framework import serializers


class StatisticsSerializer(serializers.Serializer):
    task_per_status = ...
