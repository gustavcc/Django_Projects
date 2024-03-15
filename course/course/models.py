from django.db import models

class Question(models.Model):
    
    CORRECT = (
        ('answer_1','Answer_1'),
        ('answer_2','Answer_2'),
        ('answer_3','Answer_3'),
        ('answer_4','Answer_4'),
        ('answer_5','Answer_5'),
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