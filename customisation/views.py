from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from .forms import AccessoryRequestForm
from rocks.models import Rock
from .models import Accessories


def customisation(request, rock_id):
    '''
    View for the customisation page
    '''

    rock = get_object_or_404(Rock, pk=rock_id)
    accessories = Accessories.objects.filter(type="accessory")
    frames = Accessories.objects.filter(type="frame")
    user = request.user
    user_notes = rock.user_notes

    # Only allow the user to customise a rock if they're its owner
    if user != rock.owner:
        messages.warning(request,
                         "Only the owner of this rock can customise it. "
                         "If you are the owner of this rock, please log "
                         "in using the account you used to adopt it!")
        return redirect(reverse('account_login'))

    if request.method == "POST":

        # get the selected accessories, frame, and user notes from the form
        selected_accessories = request.POST.getlist('accessory')
        selected_frame = request.POST.get('frame')
        user_notes = request.POST.get('usernotes')

        # make sure accessory id is a valid integer
        selected_accessories = [
            int(x) for x in selected_accessories if x.isdigit()
        ]

        # save the information about the selected accessories
        # in a json / dictionary
        customisation_json = {
            'accessories': selected_accessories,
            'frame': (
                int(selected_frame)
                if selected_frame and selected_frame != 'frame_none'
                else None
            ),
        }

        # bind the information to the rock and save it
        rock.accessories = customisation_json
        rock.user_notes = user_notes
        rock.save()

        messages.success(request, "Changes saved!")
        return redirect('customisation', rock_id=rock.id)

    # retrieve the current, saved accessories from the rock object
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


@login_required
def accessory_request(request):
    '''
    A view for the accessory request form
    '''

    form = AccessoryRequestForm()

    if request.method == "POST":
        # use the data from the existing html form and bind
        # them to the form in the backend for validation
        form = AccessoryRequestForm(request.POST, request.FILES)

        # after validating the form, but before submitting it, add the
        # current user to it as the sender
        if form.is_valid():
            accessory_request = form.save(commit=False)
            accessory_request.user = request.user
            accessory_request.save()
            messages.success(
                request, "Accessory request submitted. Thank you!"
                )
            return redirect(reverse('myprofile'))
        else:
            messages.error(
                request, "Uh-oh, something's not quite right. "
                "Please fix the highlighted fields and try again!"
                )

    return render(
        request, 'customisation/accessory_request.html', {'form': form}
        )
