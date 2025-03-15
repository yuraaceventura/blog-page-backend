from django.db import models
from django.utils import timezone

# Create your models here.
class BlogModel(models.Model):
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=400)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    