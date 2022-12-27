from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
