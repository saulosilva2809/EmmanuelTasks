from django.contrib import admin

from .models import TeamModel, TeamMemberModel


class TeamMemberInline(admin.TabularInline):
    model = TeamMemberModel
    extra = 1  # Quantidade de linhas vazias para novos membros

@admin.register(TeamModel)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'manager', 'created_at']
    list_filter = ['created_at']
    inlines = [TeamMemberInline] # Adiciona a lista de membros aqui

@admin.register(TeamMemberModel)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'team', 'project', 'role', 'permission_related_project', 'created_at']
    list_filter = ['role', 'team', 'project']
