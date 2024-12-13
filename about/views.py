from django.shortcuts import render


def about(request):
    '''
    View for the about page
    '''

    return render(request, 'about/about.html', {'active_page': 'about'})
