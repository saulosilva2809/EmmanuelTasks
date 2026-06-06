from rest_framework import serializers


# SERIALIZERS AUXILIARES

class ItemsSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()


class AsMemberManagerSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    items = ItemsSerializer(many=True)


# SERIALIZER PRINCIPAL 

class TeamsSerializer(serializers.Serializer):
    as_member = AsMemberManagerSerializer()
    as_manager = AsMemberManagerSerializer()
