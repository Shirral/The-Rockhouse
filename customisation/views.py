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

        print(selected_accessories)
        print(selected_frame)

        customisation_json = {
            'accessories': selected_accessories,
            'frame': selected_frame if selected_frame != 'frame_none' else None,
        }

        rock.accessories = customisation_json
        rock.save()

        return redirect('customisation', rock_id=rock.id)

    context = {
        'rock': rock,
        'accessories': accessories,
        'frames': frames
    }

    return render(request, 'customisation/customisation.html', context)
