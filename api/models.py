from django.db import models

# Create your models here.
class theyyam(models.Model):
    theyyam = models.TextField(primary_key=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.theyyam