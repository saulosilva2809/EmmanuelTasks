from django.contrib import admin

from .models import InvitationModel


@admin.register(InvitationModel)
class InvitationModelAdmin(admin.ModelAdmin):
    list_display = ['made_by', 'made_for', 'project', 'team', 'role', 'status']
    list_filter = ['made_by', 'made_for', 'project', 'team', 'role', 'status']
