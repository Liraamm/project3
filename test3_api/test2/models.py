from django.db import models

class Comment(models.Model):
    username=models.CharField(max_length=20)
    commentary = models.CharField(max_length=40)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'comment by user: {self.username}'
