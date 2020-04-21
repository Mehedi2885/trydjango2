from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home_view(request, *args, **kwargs):
    print(*args, **kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello world from home</h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is all about my project",
        "my_number": 2,
        "my_projects": ['First Project', 'Second Project'],
    }
    return render(request, "about.html", my_context)
