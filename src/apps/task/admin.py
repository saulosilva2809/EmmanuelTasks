from django.contrib import admin

from .models import TaskModel


@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'project', 'team', 'status', 'completed_at', 'priority', 'responsible', 'due_date']
    list_filter = ['status', 'completed_at', 'priority', 'project', 'team']
    search_fields = ['title', 'completed_at', 'description']
    list_editable = ['status', 'priority', 'responsible'] # permite editar direto na lista!
    date_hierarchy = 'due_date' # cria um navegador por datas no topo
