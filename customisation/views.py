from django.shortcuts import render, get_object_or_404
from rocks.models import Rock


def customisation(request, rock_id):

    rock = get_object_or_404(Rock, pk=rock_id)

    context = {
        'rock': rock
    }

    return render(request, 'customisation/customisation.html', context)
