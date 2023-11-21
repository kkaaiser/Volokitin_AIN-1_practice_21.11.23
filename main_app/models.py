from django.db import models


class Tour(models.Model):
    image = models.URLField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    duration = models.TextField()

    def __str__(self):
        return self.title


class Slider(models.Model):
    image = models.URLField()

    def __str__(self):
        return self.image


