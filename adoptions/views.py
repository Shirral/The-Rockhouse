from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
from rocks.models import Rock
from .models import RockAdoption
from .forms import AdoptionForm
import stripe


def adoption_confirm(request, rock_id):
    '''
    View for the adoption-confirm page
    '''

    rock = get_object_or_404(Rock, pk=rock_id)

    # Redirect the user and show them a message
    # if a rock they're trying to adopt already has an owner
    if rock.is_owned is True:
        messages.info(
            request,
            "The rock you are trying to adopt already has an owner. "
            "Please choose a different rock!"
        )
        return redirect(reverse('adoptions'))

    context = {
        'rock': rock
    }

    return render(request, 'adoptions/adoption-confirm.html', context)


def adoption_form(request, rock_id):
    '''
    View for the adoption-form page
    '''

    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    rock = get_object_or_404(Rock, pk=rock_id)
    cost = rock.price

    # Redirect the user and show them a message if a rock
    # they're trying to adopt already has an owner
    if rock.is_owned is True:
        messages.info(
            request,
            "The rock you are trying to adopt already has an owner. "
            "Please choose a different rock!"
        )
        return redirect(reverse('adoptions'))

    if request.method == 'POST':
        # Gather the form data in a dictionary
        form_data = {
            'full_name': request.POST['full_name'],
            'address1': request.POST['address1'],
            'address2': request.POST['address2'],
            'postcode': request.POST['postcode'],
            'town': request.POST['town'],
            'country': request.POST['country'],
        }

        # Validate the form and save it, but don't submit yet
        adoption_form = AdoptionForm(form_data)
        if adoption_form.is_valid():
            adoption = adoption_form.save(commit=False)

            # add additional information to the form data before submitting it
            adoption.rock = rock
            adoption.user = request.user
            adoption.cost = cost
            adoption.is_paid = False
            adoption.adoption_number = adoption._generate_adoption_number()

            payment_intent_id = request.POST.get('payment_intent_id')
            adoption.stripe_id = payment_intent_id

            # get payment confirmation from Stripe's updated payment intent;
            # only proceed if the payment was successful
            stripe.api_key = stripe_secret_key
            try:
                intent = stripe.PaymentIntent.retrieve(payment_intent_id)
                if intent.status == 'succeeded':
                    adoption.is_paid = True
                else:
                    adoption.is_paid = False
            except stripe.error.StripeError:
                messages.error(
                    request,
                    "Something went wrong with processing your payment. "
                    "Please try again!"
                )

            adoption.save()

            # change the ownership status of the rock
            rock.is_owned = True
            rock.owner = request.user
            rock.save()

        return redirect(
            reverse('adoption_success', args=[adoption.adoption_number])
        )

    else:
        # prepare the form
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


def adoption_success(request, adoption_number):
    '''
    Adoption_success view - adoption confirmation page
    '''

    adoption = get_object_or_404(RockAdoption, adoption_number=adoption_number)

    messages.success(request, f'{adoption.rock} was successfully adopted!')

    template = 'adoptions/adoption-success.html'
    context = {
        'adoption': adoption
    }

    return render(request, template, context)
