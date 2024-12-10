from django.db import models
from django.contrib.auth.models import User


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


class AccessoryRequest(models.Model):

    name = models.CharField(max_length=50)
    colour = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="accessory_requests/", blank=True, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.SET(None))
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
