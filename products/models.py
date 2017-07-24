from django.db import models

from utils import get_file_path


class Product(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    image = models.FileField(upload_to=get_file_path)
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    classification = models.CharField(max_length=40)

    def __str__(self):
        return self.title
