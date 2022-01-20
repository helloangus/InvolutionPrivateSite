from django.db import models

from mdeditor.fields import MDTextField

class ExampleModel(models.Model):
    name = models.CharField(max_length=10)
    content = MDTextField()