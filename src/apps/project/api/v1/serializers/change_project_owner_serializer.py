from rest_framework import serializers


class ChangeProjectOwnerSerializer(serializers.Serializer):
    new_owner = serializers.UUIDField()
