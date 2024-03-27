from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    tags = models.CharField(max_length=100, default='') 
    writer = models.CharField(max_length=20)
    createdAt = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
    
