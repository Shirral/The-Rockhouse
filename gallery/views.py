from django.shortcuts import render
from rocks.models import Rock
from customisation.models import Accessories


def gallery(request):

    rocks = Rock.objects.filter(is_owned=True)
    accessories = Accessories.objects.filter(type="accessory")
    frames = Accessories.objects.filter(type="frame")

    context = {
        'active_page': 'gallery',
        'rocks': rocks,
        'accessories': accessories,
        'frames': frames
    }

    return render(request, 'gallery/gallery.html', context)
