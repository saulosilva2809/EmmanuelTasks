from django.db.models import Q
from rest_framework import generics, status
from rest_framework.response import Response

from apps.base.permissions import IsManagerOrOwner
from apps.invitation.api.v1.serializers import (
    ListInvitationSerializer,
    SendInvitationByEmailSerializer
)
from apps.invitation.models import InvitationModel
from apps.invitation.selectors import InvitationSelector
from apps.invitation.services import InvitationService


class SendInvitationByEmailView(generics.CreateAPIView):
    permission_classes = [IsManagerOrOwner]
    serializer_class = SendInvitationByEmailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        serializer.validated_data['made_by'] = self.request.user
    
        try:
            invitation = InvitationService.email_invitation(serializer.validated_data)
            response = ListInvitationSerializer(invitation)
    
            return Response(response.data, status=status.HTTP_200_OK)
    
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ViewInvitationByEmailView(generics.ListAPIView):
    lookup_url_kwarg = 'link'
    lookup_field = 'link'
    permission_classes = [IsManagerOrOwner]

    def get_queryset(self):
        return InvitationSelector.get_by_user(self.request.user)
    
    def list(self, request, *args, **kwargs):
        response = ListInvitationSerializer(self.get_object())
    
        return Response(response.data, status=status.HTTP_200_OK)


class AcceptInvitationView(generics.GenericAPIView):
    lookup_field = 'link'
    lookup_url_kwarg = 'link'
    permission_classes = [IsManagerOrOwner]

    def get_queryset(self):
        return InvitationSelector.get_by_user(self.request.user)
    
    def post(self, request, *args, **kwargs):
        self.check_object_permissions(request, self.get_object())
        invitation = InvitationService.accept_invitation(
            self.get_object(),
            self.request.user
        )
        response = ListInvitationSerializer(invitation)
    
        return Response(response.data, status=status.HTTP_200_OK)


class DeclineInvitationView(generics.GenericAPIView):
    lookup_field = 'link'
    lookup_url_kwarg = 'link'
    permission_classes = [IsManagerOrOwner]

    def get_queryset(self):
        return InvitationSelector.get_by_user(self.request.user)
    
    def post(self, request, *args, **kwargs):
        self.check_object_permissions(request, self.get_object())
        invitation = InvitationService.decline_invitation(
            self.get_object(),
            self.request.user
        )
        response = ListInvitationSerializer(invitation)
    
        return Response(response.data, status=status.HTTP_200_OK)
