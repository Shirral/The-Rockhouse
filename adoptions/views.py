from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from rocks.models import Rock
from .models import RockAdoption
from .forms import AdoptionForm
import stripe


def adoption_confirm(request, rock_id):

    rock = get_object_or_404(Rock, pk=rock_id)

    context = {
        'rock': rock
    }

    return render(request, 'adoptions/adoption-confirm.html', context)


def adoption_form(request, rock_id):

    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    rock = get_object_or_404(Rock, pk=rock_id)
    cost = rock.price

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST['full_name'],
            'address1': request.POST['address1'],
            'address2': request.POST['address2'],
            'postcode': request.POST['postcode'],
            'town': request.POST['town'],
            'country': request.POST['country'],
        }

        adoption_form = AdoptionForm(form_data)
        if adoption_form.is_valid():
            adoption = adoption_form.save(commit=False)

            adoption.rock = rock
            adoption.user = request.user
            adoption.cost = cost
            adoption.is_paid = False  # updated later with webhook?
            adoption.adoption_number = adoption._generate_adoption_number()

            # get stripe id from the PI - change later to get it from webhook
            # if time!
            payment_intent_id = request.POST.get('payment_intent_id')
            adoption.stripe_id = payment_intent_id

            # get payment confirmation from the PI - change later to get it
            # from webhook if time! - from
            # https://docs.stripe.com/api/payment_intents/retrieve ,
            # error handling:
            # https://docs.stripe.com/error-handling?lang=python&locale=en-GB#catch-exceptions
            stripe.api_key = stripe_secret_key
            try:
                intent = stripe.PaymentIntent.retrieve(payment_intent_id)
                if intent.status == 'succeeded':
                    adoption.is_paid = True
                else:
                    adoption.is_paid = False
            except stripe.error.StripeError as e:
                messages.error(request, "Something went wrong. Please try again!")

            adoption.save()

        return redirect(reverse('adoption_success', args=[adoption.id]))

    else:
        stripe_cost = round(cost * 100)
        adoption_form = AdoptionForm()
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_cost,
            currency=settings.STRIPE_CURRENCY
        )

        context = {
            'rock': rock,
            'adoption_form': adoption_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
            'payment_intent_id': intent.id
        }

        return render(request, 'adoptions/adoption-form.html', context)
