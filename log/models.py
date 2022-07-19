from django.db import models
from publicararte.models import Arte
from django.contrib.auth.models import User

# Create your models here.
class Log(models.Model):
    message = models.TextField()
