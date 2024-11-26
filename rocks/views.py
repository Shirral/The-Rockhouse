from django.shortcuts import render, get_object_or_404
from .models import Rock


def adoptions(request):

    rocks = Rock.objects.all()

    context = {
        'active_page': 'adoptions',
        'rocks': rocks
    }

    return render(request, 'rocks/index.html', context)


def rockprofile(request, rock_id):

    rock = get_object_or_404(Rock, pk=rock_id)

    context = {
        'rock': rock
    }

    return render(request, 'rocks/rockprofile.html', context)
