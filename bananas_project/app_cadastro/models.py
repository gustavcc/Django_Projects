from django.db import models

# Create your models here.

class Corte(models.Model):
    id_corte = models.AutoField(primary_key=True)
    primeira = models.IntegerField()
    segunda = models.IntegerField()
    