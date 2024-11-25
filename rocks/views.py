from django.shortcuts import render
from .models import Rock


def adoptions(request):

    rocks = Rock.objects.all()

    context = {
        'active_page': 'adoptions',
        'rocks': rocks

    }

    return render(request, 'rocks/index.html', context)
