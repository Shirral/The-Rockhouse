from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Rock
from .forms import RockEditForm
from customisation.models import Accessories


def adoptions(request):
    '''
    View for the available adoptions page (homepage)
    '''

    rocks = Rock.objects.filter(is_owned=False)

    context = {
        'active_page': 'adoptions',
        'rocks': rocks,
    }

    return render(request, 'rocks/index.html', context)


def rockprofile(request, rock_id):
    '''
    View for the rock profile page
    '''

    rock = get_object_or_404(Rock, pk=rock_id)
    accessories = Accessories.objects.filter(type="accessory")
    frames = Accessories.objects.filter(type="frame")

    # retrieve currently selected accessories saved in the rock object
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
    '''
    A view for the rock edit admin-only page
    '''

    rock = get_object_or_404(Rock, pk=rock_id)
    users = User.objects.all()
    accessories = Accessories.objects.filter(type="accessory")
    frames = Accessories.objects.filter(type="frame")

    form = RockEditForm(instance=rock)

    # only allow superusers to access the page
    if not request.user.is_superuser:
        messages.info(
            request,
            "The page you are trying to access is only available "
            "to site administrators. Sorry!"
        )
        return redirect(reverse('rockprofile', kwargs={'rock_id': rock_id}))

    # retrieve currently selected accessories saved in the rock object
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

        # validate the frontend form using the backend
        # form & model and save the information
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
    '''
    Admin-only view for deleting the rocks
    '''

    if not request.user.is_superuser:
        messages.info(
            request,
            "The page you are trying to access is only available "
            "to site administrators. Sorry!"
        )
        return redirect(reverse('rockprofile', kwargs={'rock_id': rock_id}))

    if request.method == "POST":
        rock = get_object_or_404(Rock, id=rock_id)
        rock.delete()
        messages.success(request, "Rock deleted successfully!")
        return redirect("adoptions")
