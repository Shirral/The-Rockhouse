from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Rock
from .forms import RockEditForm
from customisation.models import Accessories


def adoptions(request):

    rocks = Rock.objects.filter(is_owned=False)
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


def rock_edit(request, rock_id):

    rock = get_object_or_404(Rock, pk=rock_id)
    users = User.objects.all()
    accessories = Accessories.objects.filter(type="accessory")
    frames = Accessories.objects.filter(type="frame")

    form = RockEditForm(instance=rock)

    if rock.accessories and rock.accessories != "None":
        selected_accessories = rock.accessories['accessories']
        if rock.accessories['frame']:
            selected_frame = int(rock.accessories['frame'])
        else:
            selected_frame = 'None'
    else:
        selected_accessories = []
        selected_frame = 'None'

    if request.method == "POST":

        form = RockEditForm(request.POST, instance=rock)

        if form.is_valid():
            form.save()
            messages.success(request, "Rock details updated!")
            return redirect("rockprofile", rock_id=rock.id)
        else:
            messages.error(request,
                           "Uh-oh, something's not quite right. "
                           "Please fix the highlighted fields and "
                           "try again!")

    context = {
        'rock': rock,
        'users': users,
        'accessories': accessories,
        'frames': frames,
        'selected_frame': selected_frame,
        'selected_accessories': selected_accessories,
        'form': form
    }

    return render(request, 'rocks/rock-edit.html', context)


def rock_delete(request, rock_id):
    if request.method == "POST":
        rock = get_object_or_404(Rock, id=rock_id)
        rock.delete()
        messages.success(request, "Rock deleted successfully!")
        return redirect("adoptions")
