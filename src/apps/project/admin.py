from django.contrib import admin

from apps.sprint.models import SprintModel
from .models import ProjectModel


class SprintInline(admin.TabularInline):
    model = SprintModel
    extra = 0
    fields = ['name', 'status', 'start_date', 'end_date']
    show_change_link = True # cria um link para editar a sprint direto daqui


@admin.register(ProjectModel)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'owner', 'start_date', 'term']
    list_filter = ['status', 'owner']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)} # Ajuda a visualizar o slug no admin
    inlines = [SprintInline]
