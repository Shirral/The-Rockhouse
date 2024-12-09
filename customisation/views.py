from django.shortcuts import render, get_object_or_404, redirect
from rocks.models import Rock
from .models import Accessories


def customisation(request, rock_id):

    rock = get_object_or_404(Rock, pk=rock_id)
    accessories = Accessories.objects.filter(type="accessory")
    frames = Accessories.objects.filter(type="frame")

    if request.method == "POST":

        selected_accessories = request.POST.getlist('accessory')
        selected_frame = request.POST.get('frame')

        for x in range(len(selected_accessories)):
            selected_accessories[x] = int(selected_accessories[x])

        # print(selected_accessories)
        # print(selected_frame)

        customisation_json = {
            'accessories': selected_accessories,
            'frame': int(selected_frame) if selected_frame != 'frame_none' else None,
        }

        rock.accessories = customisation_json
        rock.save()

        return redirect('customisation', rock_id=rock.id)

    if rock.accessories != "":
        selected_accessories = rock.accessories['accessories']
        print(selected_accessories)
        if rock.accessories['frame']:
            selected_frame = int(rock.accessories['frame'])
        else:
            selected_frame = 'None'
        print(selected_frame)

    context = {
        'rock': rock,
        'accessories': accessories,
        'frames': frames,
        'selected_frame': selected_frame,
        'selected_accessories': selected_accessories
    }

    return render(request, 'customisation/customisation.html', context)
