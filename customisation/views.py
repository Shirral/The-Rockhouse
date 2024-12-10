from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from rocks.models import Rock
from .models import Accessories


def customisation(request, rock_id):

    rock = get_object_or_404(Rock, pk=rock_id)
    accessories = Accessories.objects.filter(type="accessory")
    frames = Accessories.objects.filter(type="frame")
    user = request.user
    user_notes = rock.user_notes

    if user != rock.owner:
        messages.warning(request, "Only the owner of this rock can customise it. If you are the owner of this rock, please log in using the account you used to adopt it!")
        return redirect(reverse('adoptions'))

    if request.method == "POST":

        selected_accessories = request.POST.getlist('accessory')
        selected_frame = request.POST.get('frame')
        user_notes = request.POST.get('usernotes')

        selected_accessories = [int(x) for x in selected_accessories if x.isdigit()]

        customisation_json = {
            'accessories': selected_accessories,
            'frame': int(selected_frame) if selected_frame and selected_frame != 'frame_none' else None,
        }

        rock.accessories = customisation_json
        rock.user_notes = user_notes
        rock.save()

        return redirect('customisation', rock_id=rock.id)

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
        'selected_accessories': selected_accessories,
        'user_notes': user_notes
    }

    return render(request, 'customisation/customisation.html', context)


def accessory_request(request):

    return render(request, 'customisation/accessory_request.html')