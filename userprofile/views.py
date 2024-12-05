from django.shortcuts import render, get_object_or_404
from rocks.models import Rock
from adoptions.models import RockAdoption
from django.contrib.auth.models import User


def profile(request, username):

    user = get_object_or_404(User, username__iexact=username)
    user_id = user.id
    rock_adoption = RockAdoption.objects.filter(user=user_id)
    rock_number = len(rock_adoption)

    context = {
        'user': user,
        'rock_number': rock_number,
        'rock_adoption': rock_adoption
    }

    return render(request, 'userprofile/profile.html', context)
