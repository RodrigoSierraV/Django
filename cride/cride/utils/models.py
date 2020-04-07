from django.db import models


class CRideModel(models.Model):
    """
        Abstract base class to other models
        This class provides tables with these attributes:
            created (DateTime): Stores when the object was created
            modified (DateTime): Stores last time when the object was modified
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time when the object was created'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time when the object was last modified'
    )

    class Meta:
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']