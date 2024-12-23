import os
from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User


# Accessories model
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

    # fix the model name displaying incorrectly in Django admin
    class Meta:
        verbose_name_plural = "Accessories"

    # display visual previews of accessories in Django admin
    def image_tag(self):
        if self.image:
            if 'USE_AWS' in os.environ:
                return mark_safe(
                    '<img src="https://the-rockhouse.s3.amazonaws.com/media/%s"'
                    ' width="150" height="150" />' % (self.image)
                )
            else:
                return mark_safe(
                    '<img src="/media/%s" width="150" height="150" '
                    '/>' % (self.image)
                )
        return "(No image)"

    image_tag.short_description = 'Image'


# AccessoryRequest model
class AccessoryRequest(models.Model):

    name = models.CharField(max_length=50)
    colour = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(max_length=50)
    description = models.TextField(max_length=600)
    image = models.ImageField(
        upload_to="accessory_requests/", blank=True, null=True
        )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    user = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.SET(None)
        )
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
