from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.get_index, name='index'),
    path('<str:url_items>/', views.get_items_menu, name='items_menu'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                           document_root=settings.STATIC_ROOT)

