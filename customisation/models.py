from django.db import models


class Accessories(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    colour = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    rock_shape = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
