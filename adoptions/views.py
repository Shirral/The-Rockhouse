from django.shortcuts import render, get_object_or_404
from django.conf import settings
from rocks.models import Rock
from .forms import AdoptionForm


def adoption_confirm(request, rock_id):

    rock = get_object_or_404(Rock, pk=rock_id)

    context = {
        'rock': rock
    }

    return render(request, 'adoptions/adoption-confirm.html', context)


def adoption_form(request, rock_id):

    rock = get_object_or_404(Rock, pk=rock_id)
    adoption_form = AdoptionForm()
    stripe_public_key = stripe_public_key = settings.STRIPE_PUBLIC_KEY

    context = {
        'rock': rock,
        'adoption_form': adoption_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': 'test client secret'
    }

    return render(request, 'adoptions/adoption-form.html', context)
