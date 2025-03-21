from django.db import models

# Create your models here.
class Component(models.Model):
    name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    description = models.TextField(default='')
    category = models.ManyToManyField('category.Category', blank=False)
    manufacturer = models.ForeignKey('manufacturer.Manufacturer', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock = models.IntegerField(default=0)
    drawer = models.ForeignKey('drawer.Drawer', null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name