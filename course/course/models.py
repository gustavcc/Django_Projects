from django.db import models

class Question(models.Model):
    
    CORRECT = (
        ('A','A)'),
        ('B','B)'),
        ('C','C)'),
        ('D','D)'),
        ('E','E)'),
    )
    
    title = models.TextField()
    answer_a = models.CharField(max_length=255, default='')
    answer_b = models.CharField(max_length=255, default='')
    answer_c = models.CharField(max_length=255, default='')
    answer_d = models.CharField(max_length=255, default='')
    answer_e = models.CharField(max_length=255, default='')
    
    correct = models.CharField(max_length=8, choices=CORRECT)
    
    def __str__(self):
        return self.title