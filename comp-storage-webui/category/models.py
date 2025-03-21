from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    description = models.TextField(default='', blank=True, null=True)
    parent = models.ManyToManyField('self', blank=True, null=True, symmetrical=False, related_name='children')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name