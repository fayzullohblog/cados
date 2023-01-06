from django.db import models

# Create your models here.
class Advocate(models.Model):
    username=models.CharField(max_length=200)
    bio=models.TextField(max_length=250)

    def __str__(self) -> str:
        return self.username