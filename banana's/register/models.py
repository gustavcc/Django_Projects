from django.db import models

class Cut(models.Model):
    cut_first = models.IntegerField()
    cut_second = models.IntegerField()