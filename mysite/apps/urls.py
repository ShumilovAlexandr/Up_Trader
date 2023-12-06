from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.get_index, name='index'),
    # path('/<str:slug>')
    # TODO это в уроке для динамических страниц (посмотри 22
    #  урок для начала
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                           document_root=settings.STATIC_ROOT)

