from django.shortcuts import render, get_object_or_404
from rocks.models import Rock
from .forms import AdoptionForm

from django.template.loader import engines
template_dirs = engines['django'].dirs
print("Template directories Django is searching:")
for directory in template_dirs:
    print(directory)


def adoption_confirm(request, rock_id):

    rock = get_object_or_404(Rock, pk=rock_id)

    context = {
        'rock': rock
    }

    return render(request, 'adoptions/adoption-confirm.html', context)


def adoption_form(request, rock_id):

    rock = get_object_or_404(Rock, pk=rock_id)
    adoption_form = AdoptionForm()

    context = {
        'rock': rock,
        'adoption_form': adoption_form
    }

    return render(request, 'adoptions/adoption-form.html', context)
