from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name