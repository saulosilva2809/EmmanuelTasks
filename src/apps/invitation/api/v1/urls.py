from django.urls import path

from apps.invitation.api.v1.views import (
    AcceptInvitationView,
    DeclineInvitationView,
    SendInvitationByEmailView,
    ViewInvitationByEmailView
)


urlpatterns = [
    path(
        'by-email/', 
        view=SendInvitationByEmailView.as_view(),
        name='send_invitation_by_email_view'
    ),
    path(
        '<uuid:link>/',
        view=ViewInvitationByEmailView.as_view(),
        name='view_invitation_by_email_view'
    ),
    path(
        '<uuid:link>/accept/',
        view=AcceptInvitationView.as_view(),
        name='accept_invitation_view'
    ),
    path(
        '<uuid:link>/decline/',
        view=DeclineInvitationView.as_view(),
        name='decline_invitation_view'
    ),
]
