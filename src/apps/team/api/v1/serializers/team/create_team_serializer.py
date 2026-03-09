from rest_framework import serializers

from apps.authentication.models import UserModel
from apps.team.models import TeamModel


class CreateTeamSerializer(serializers.ModelSerializer):
    manager = serializers.PrimaryKeyRelatedField(
        queryset=UserModel.objects.all(), 
        required=False, 
        allow_null=True
    )

    class Meta:
        model = TeamModel
        fields = ('id', 'name', 'description', 'manager')
        read_only_fields = ['id']
