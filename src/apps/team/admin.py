from django.contrib import admin

from .models import TeamModel

@admin.register(TeamModel)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'manager', 'created_at']
    search_fields = ['name']
    filter_horizontal = ['members'] # cria caixa de seleção lateral
