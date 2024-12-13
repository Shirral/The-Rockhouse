from django.db import models
from django.contrib.auth.models import User


# Rock model
class Rock(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()
    short_description = models.TextField()
    user_notes = models.TextField(null=True, blank=True, max_length=800)
    is_owned = models.BooleanField(default=False)
    owner = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL
        )
    material = models.CharField(max_length=50)
    texture = models.CharField(max_length=50)
    personality = models.CharField(max_length=50)
    shape = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    accessories = models.JSONField(null=True, blank=True)
    image = models.ImageField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
