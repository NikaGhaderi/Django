from django.http import HttpResponse
from django.shortcuts import render


# you wanna make sure that your logic is already handled in view. conventional


def home_view(request, *args, **kwargs):
    print(request.user)
    print(args, kwargs)
    #return HttpResponse("<h1>hello world!</h1>")
    return render(request, "home.html", {})


def main_view(request):
    my_context = {
        "title": 'this is about us',
        'my_html': '<p  style="font-weight: bold; color: #894fa2">I\'m actually an html, not a text</p>',
        "my_number": 123,
        "abc": True,
        "my_list": [
            1,
            2,
            3,
        ]
    }
    return render(request, "main.html", my_context)