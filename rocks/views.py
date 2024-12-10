from django.shortcuts import render, get_object_or_404
from .models import Rock
from customisation.models import Accessories


def adoptions(request):

    rocks = Rock.objects.all()
    accessories = Accessories.objects.filter(type="accessory")
    frames = Accessories.objects.filter(type="frame")

    context = {
        'active_page': 'adoptions',
        'rocks': rocks,
        'accessories': accessories,
        'frames': frames
    }

    return render(request, 'rocks/index.html', context)


def rockprofile(request, rock_id):

    rock = get_object_or_404(Rock, pk=rock_id)
    accessories = Accessories.objects.filter(type="accessory")
    frames = Accessories.objects.filter(type="frame")

    if rock.accessories and rock.accessories != "None":
        selected_accessories = rock.accessories['accessories']
        if rock.accessories['frame']:
            selected_frame = int(rock.accessories['frame'])
        else:
            selected_frame = 'None'
    else:
        selected_accessories = []
        selected_frame = 'None'

    context = {
        'rock': rock,
        'accessories': accessories,
        'frames': frames,
        'selected_frame': selected_frame,
        'selected_accessories': selected_accessories
    }

    return render(request, 'rocks/rockprofile.html', context)
