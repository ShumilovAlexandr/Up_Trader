from django.shortcuts import render


def get_index(request):
    return render(request,
                  "templates/index.html")


def get_items_menu(request, url_items):
    pass
