from rest_framework import serializers

from apps.invitation.models import InvitationModel


class SendInvitationByEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitationModel
        fields = ['made_for', 'project', 'team']
