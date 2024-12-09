from django.shortcuts import render, get_object_or_404, redirect, reverse
from adoptions.models import RockAdoption
from customisation.models import Accessories
from django.contrib.auth.models import User


def profile(request, username):

    user = get_object_or_404(User, username__iexact=username)
    user_id = user.id
    rock_adoption = RockAdoption.objects.filter(user=user_id)
    rock_number = len(rock_adoption)
    accessories = Accessories.objects.filter(type="accessory")
    frames = Accessories.objects.filter(type="frame")

    # for rock in rock_adoption.rock:
    #     if rock_adoption.rock.accessories != "":
    #         selected_accessories = rock_adoption.rock.accessories['accessories']
    #         if rock_adoption.rock.accessories['frame']:
    #             selected_frame = int(rock_adoption.rock.accessories['frame'])
    #         else:
    #             selected_frame = 'None'

    # did not work, gotta try the templates

    context = {
        'user': user,
        'rock_number': rock_number,
        'rock_adoption': rock_adoption,
        'accessories': accessories,
        'frames': frames,
        # 'selected_frame': selected_frame,
        # 'selected_accessories': selected_accessories
    }

    return render(request, 'userprofile/profile.html', context)


def myprofile(request):

    username = request.user.username

    return redirect(reverse(profile, args=[username]))
