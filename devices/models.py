from django.db import models
from farming.models import Plot


# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=20)
    mac_address = models.CharField(max_length=20)
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    last_updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    last_updated_by = models.CharField(max_length=100)

    # ...
    def __str__(self):
        return self.name, self.mac_address
