from django.shortcuts import render, get_object_or_404
from rocks.models import Rock

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




