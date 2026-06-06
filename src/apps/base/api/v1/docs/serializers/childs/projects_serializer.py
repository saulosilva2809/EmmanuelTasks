from rest_framework import serializers


# SERIALIZERS AUXILIARES

class ItemsSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()


class AsMemberOwnerSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    items = ItemsSerializer(many=True)


# SERIALIZER PRINCIPAL 

class ProjectsSerializer(serializers.Serializer):
    as_member = AsMemberOwnerSerializer()
    as_owner = AsMemberOwnerSerializer()
