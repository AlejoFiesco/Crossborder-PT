from django.db import models

# Create your models here.
class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    score = models.FloatField()

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, country: {self.country}, score: {self.score}'