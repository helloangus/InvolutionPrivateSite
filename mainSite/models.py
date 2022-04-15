from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    project_name = models.CharField(max_length=50)
    project_img = models.ImageField(upload_to = 'prj_img')

    project_theme = models.CharField(max_length=200)
    project_content = models.CharField(max_length=99999)

    pub_date = models.DateTimeField('date published')


