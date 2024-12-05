from django.shortcuts import render, get_object_or_404
from rocks.models import Rock
from adoptions.models import RockAdoption
from django.contrib.auth.models import User


def profile(request, username):

    user = get_object_or_404(User, username__iexact=username)
    user_id = user.id
    rocks = Rock.objects.filter(owner=user_id)
    rock_number = len(rocks)
    # adoption_date = only that from RockAdoption? Or the above, too?

    context = {
        'user': user,
        'rocks': rocks,
        'rock_number': rock_number
    }

    return render(request, 'userprofile/profile.html', context)
