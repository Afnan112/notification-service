from django.db import models

# Create your models here.
class Notification(models.Model):
    user_id = models.CharField(max_length=10)
    channel = models.CharField(max_length=50)
    template = models.CharField(max_length=100)
    data = models.JSONField()
    status = models.CharField(max_length=20, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self. user_id