from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class signedData(models.Model):
    name = models.CharField(max_length=200, blank=True, default='')
    file_name=models.CharField(max_length=80, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['created_at']
        db_table = 'Signed_data'
        verbose_name_plural='Signed_Data'

    def __str__(self):
        return self.name



class CustomUser(AbstractUser):
    role=models.CharField(max_length=7)
    class Meta:
        db_table='User'

