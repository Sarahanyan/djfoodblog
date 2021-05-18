from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path

# Create your views here.


def home_view(request):
    print(settings.BASE_DIR)
    print(Path(settings.BASE_DIR) / 'staticfiles')
    print(Path(__file__).resolve())
    directory = Path(settings.BASE_DIR).parent
    template = "index.html"
    context = {
        "directo": Path(settings.BASE_DIR / "staticfiles")
    }
    return render(request, template, context)


def about_view(request):
    template = "about.html"
    return render(request, template, context)


def contact_view(request):
    template = "contact.html"
    return render(request, template, context)
