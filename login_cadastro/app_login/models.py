from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    username = models.TextField(max_length=255)
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)