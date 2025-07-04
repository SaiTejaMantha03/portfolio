
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    repo_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title
