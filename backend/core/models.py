from django.db import models


class Title(models.Model):
    name = models.CharField(max_length=128)
    year = models.PositiveSmallIntegerField()
    descriptions = models.TextField()
    episode = models.SmallIntegerField()

    class Meta:
        unique_together = [
            ("name", "year")
        ]
