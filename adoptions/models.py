import uuid
from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from rocks.models import Rock


class RockAdoption(models.Model):

    # information about the adoption
    rock = models.ForeignKey(Rock, null=False, blank=False, on_delete=models.PROTECT)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.SET(None))
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    stripe_id = models.CharField(max_length=254, null=False, blank=False, default='')
    adoption_number = models.CharField(max_length=32, null=False, editable=False)
    date = models.DateField(auto_now_add=True)

    # billing information for Stripe
    full_name = models.CharField(max_length=50, null=False, blank=False)
    address1 = models.CharField(max_length=80, null=False, blank=False)
    address2 = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town = models.CharField(max_length=40, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)

    def _generate_adoption_number(self):
        """
        Generate a random, unique order number using UUID. Function
        code taken from Code Institute's Boutique Ado student project.
        """
        return uuid.uuid4().hex.upper()

    def __str__(self):
        """Return basic information about the adoption"""
        return f"{self.user or 'Deleted User'} adopted {self.rock} on {self.date}"
