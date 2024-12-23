from django.shortcuts import render, get_object_or_404, redirect, reverse
from adoptions.models import RockAdoption
from customisation.models import Accessories
from django.contrib.auth.models import User


def profile(request, username):
    '''
    View for the user profile page
    '''

    user = get_object_or_404(User, username__iexact=username)
    user_id = user.id
    rock_adoption = RockAdoption.objects.filter(user=user_id)
    rock_number = len(rock_adoption)
    accessories = Accessories.objects.filter(type="accessory")
    frames = Accessories.objects.filter(type="frame")

    context = {
        'user': user,
        'rock_number': rock_number,
        'rock_adoption': rock_adoption,
        'accessories': accessories,
        'frames': frames,
    }

    return render(request, 'userprofile/profile.html', context)


def myprofile(request):
    '''
    View directing users to their own profile page
    '''

    username = request.user.username

    return redirect(reverse(profile, args=[username]))
