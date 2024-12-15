from django.db import models

# Create your models here.
class Developer(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Games(models.Model):
    title = models.CharField(max_length=50)
    developer = models.ForeignKey(to=Developer, on_delete=models.PROTECT)
