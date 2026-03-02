from django.db import models
from django.utils import timezone


class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        return super().update(deleted_at=timezone.now())

    def hard_delete(self):
        return super().delete()

    def active(self):
        return self.filter(deleted_at__isnull=True)

    def deleted(self):
        return self.filter(deleted_at__isnull=False)


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db).filter(
            deleted_at__isnull=True
        )


class SoftDeleteModel(models.Model):
    deleted_at = models.DateTimeField(null=True, blank=True)

    # Managers
    objects = SoftDeleteManager()              # padrão → só ativos
    all_objects = SoftDeleteQuerySet.as_manager()  # acesso total

    class Meta:
        abstract = True

    # Soft delete individual
    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save(update_fields=['deleted_at'])

    # Hard delete real
    def hard_delete(self):
        super().delete()

    # Restore
    def restore(self):
        self.deleted_at = None
        self.save(update_fields=['deleted_at'])
