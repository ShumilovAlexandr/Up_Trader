from django.shortcuts import (render,
                              get_object_or_404)
from django.http import HttpResponse

from .models import SubTitle


def get_index(request):
    return render(request,
                  "templates/index.html")


def show_page(request, page_slug):
    page = get_object_or_404(SubTitle, slug=page_slug)

    data = {
        'page': page,
        'page_slug': page_slug
    }
    return render(request, 'templates/page.html', data)

