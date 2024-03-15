from django.db import models

class Question(models.Model):
    
    CORRECT = (
        ('answer_1','a)'),
        ('answer_2','b)'),
        ('answer_3','c)'),
        ('answer_4','d)'),
        ('answer_5','e)'),
    )
    
    title = models.TextField()
    answer_1 = models.CharField(max_length=255, default='a)')
    answer_2 = models.CharField(max_length=255,default='b)')
    answer_3 = models.CharField(max_length=255,default='c)')
    answer_4 = models.CharField(max_length=255,default='d)')
    answer_5 = models.CharField(max_length=255,default='e)')
    
    correct = models.CharField(max_length=8, choices=CORRECT)
    
    def __str__(self):
        return self.title