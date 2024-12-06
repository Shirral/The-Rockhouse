from django.shortcuts import render, get_object_or_404
from rocks.models import Rock
from .models import Accessories


def customisation(request, rock_id):

    rock = get_object_or_404(Rock, pk=rock_id)
    accessories = Accessories.objects.filter(type="accessory")
    frames = Accessories.objects.filter(type="frame")

    context = {
        'rock': rock,
        'accessories': accessories,
        'frames': frames
    }

    return render(request, 'customisation/customisation.html', context)
