from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, "home.html")


def blog(request):
    return render(request, "blog.html")


def handler404(request, exception):
    return render(request, "404.html", status=404)


def form(request):
    return HttpResponse("Form submitted successfully")
