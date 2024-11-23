from django.shortcuts import render


def adoptions(request):
    return render(request, 'rocks/index.html', {'active_page': 'adoptions'})
