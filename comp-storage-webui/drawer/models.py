from django.db import models

class Drawer(models.Model):

    class DrawerSize(models.TextChoices):
        WIDE1 = 'wide1', 'Wide 1'
        WIDE2 = 'wide2', 'Wide 2'
        NARROW = 'narrow', 'Narrow'
        LARGE = 'large', 'Large'
        LARGEST = 'largest', 'Largest'

    location = models.CharField(max_length=10, blank=True, null=True, unique=True)

    size = models.CharField(
        max_length=10,
        choices=DrawerSize.choices,
        default=DrawerSize.WIDE1,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField('category.Category', related_name='drawers', blank=True, null=True)

    def __str__(self):
        return self.location