from rest_framework import serializers

from apps.base.serializers import (
    ProjectMinSerializer,
    TeamMinSerializer,
    UserMinSerializer,
)
from apps.invitation.models import InvitationModel


class ListInvitationSerializer(serializers.ModelSerializer):
    made_by = UserMinSerializer(read_only=True)
    project = ProjectMinSerializer(read_only=True)
    team = TeamMinSerializer(read_only=True)
    expiration_date = serializers.DateField()

    class Meta:
        model = InvitationModel
        fields = [
            'made_by',
            'made_for',
            'project',
            'team',
            'link',
            'expiration_date',
            'status',
        ]
