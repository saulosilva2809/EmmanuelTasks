from django.contrib import admin

from apps.task.models import TaskModel
from .models import SprintModel


class TaskInline(admin.TabularInline):
    model = TaskModel
    extra = 0
    fields = ['title', 'responsible', 'status', 'priority']
    show_change_link = True


@admin.register(SprintModel)
class SprintAdmin(admin.ModelAdmin):
    list_display = ['name', 'team', 'project', 'status', 'start_date', 'end_date']
    list_filter = ['status', 'team', 'project']
    search_fields = ['name', 'goal']
    inlines = [TaskInline]
