from django.shortcuts import render, get_object_or_404
from .models import Rock
from customisation.models import Accessories


def adoptions(request):

    rocks = Rock.objects.all()
    accessories = Accessories.objects.filter(type="accessory")
    frames = Accessories.objects.filter(type="frame")

    # if rock.accessories != "":
    #     selected_accessories = rock.accessories['accessories']
    #     if rock.accessories['frame']:
    #         selected_frame = int(rock.accessories['frame'])
    #     else:
    #         selected_frame = 'None'

    # that won't work here - gotta work with the template logic;
    # {% if int(rock.accessories['frame']) != 'None' %}            ||| if (rock.accessories['frame'])|stringformat:"d" != 'None' ?
    #     {% for frame in frames %}
    #         {% if frame.id == int(rock.accessories['frame']) %}
    #         <img src="{{ frame.image.url }}" class="img-fluid accesory-checkbox custom-rounded" alt="image of {{frame.name}}" style="position: absolute; top: 0px; left: 0px; width: 100%; height: auto; z-index: 2;">
    #         {% endif %}
    #     {% endfor %}
    # {% endif %}

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

    if rock.accessories != "":
        selected_accessories = rock.accessories['accessories']
        if rock.accessories['frame']:
            selected_frame = int(rock.accessories['frame'])
        else:
            selected_frame = 'None'

    context = {
        'rock': rock,
        'accessories': accessories,
        'frames': frames,
        'selected_frame': selected_frame,
        'selected_accessories': selected_accessories
    }

    return render(request, 'rocks/rockprofile.html', context)
