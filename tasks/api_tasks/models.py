from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)