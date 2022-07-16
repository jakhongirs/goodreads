from django.http import HttpResponse


def landing_page(request):
    return HttpResponse("Django is working!")
