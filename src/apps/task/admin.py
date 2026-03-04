from django.contrib import admin

from .models import TaskModel


@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'project', 'team', 'status', 'priority', 'responsible', 'due_date']
    list_filter = ['status', 'priority', 'project', 'team']
    search_fields = ['title', 'description']
    list_editable = ['status', 'priority', 'responsible'] # permite editar direto na lista!
    date_hierarchy = 'due_date' # cria um navegador por datas no topo
