from rest_framework import serializers

from apps.authentication.models import UserModel


class UserMinSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = UserModel
        fields = ('id', 'full_name')

    def get_full_name(self, obj):
        if obj.first_name or obj.last_name:
            return f'{obj.first_name} {obj.last_name}'.strip()
        return obj.email
