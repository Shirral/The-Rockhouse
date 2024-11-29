from django.shortcuts import render, get_object_or_404
from django.conf import settings
from rocks.models import Rock
from .forms import AdoptionForm
import stripe


def adoption_confirm(request, rock_id):

    rock = get_object_or_404(Rock, pk=rock_id)

    context = {
        'rock': rock
    }

    return render(request, 'adoptions/adoption-confirm.html', context)


def adoption_form(request, rock_id):

    rock = get_object_or_404(Rock, pk=rock_id)
    cost = rock.price
    stripe_cost = round(cost * 100)
    adoption_form = AdoptionForm()
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_cost,
        currency=settings.STRIPE_CURRENCY
    )

    print(intent)

    context = {
        'rock': rock,
        'adoption_form': adoption_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }

    return render(request, 'adoptions/adoption-form.html', context)
