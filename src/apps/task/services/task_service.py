from django.db import transaction

from apps.authentication.models import UserModel
from apps.task.models import TaskModel
from apps.task.validators import validate_task_data, validate_set_task_completed


class TaskService:
    @staticmethod
    @transaction.atomic()
    def create_task(validated_data: dict):
        validate_task_data(validated_data)
        validated_data.pop('user')

        return TaskModel.objects.create(**validated_data)

    @staticmethod
    @transaction.atomic()
    def update_task(data: dict, instance: TaskModel):
        validate_task_data(data, instance)

        for field, value in data.items():
            setattr(instance, field, value)

        instance.save()
        return instance
    
    @staticmethod
    @transaction.atomic()
    def set_task_as_completed(instance: TaskModel, user: UserModel):
        validate_set_task_completed(instance, user)

        # salvar a task
        instance.status = TaskModel.TaskStatusChoices.DONE
        instance.save()

        # salvar a sprint para atualizar o progress
        instance.sprint.save()

        return instance
