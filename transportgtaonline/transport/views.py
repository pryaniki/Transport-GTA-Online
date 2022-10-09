from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count

from .models import Ground, GroundCategory, Shop


def index(request):
    transports = Ground.objects.all()
    cats = Ground.objects.values('cats__name').annotate(total=Count('id'))
    shops = Ground.objects.values('shops__name').annotate(total=Count('id'))
    context = {
        'title': 'Главная страница',
        'transports': transports,
        'cats': cats,
        'shops': shops,
    }
    return render(request, 'transport/index.html', context=context)


def show_ground_transport(request):
    transports = Ground.objects.all()
    cats = GroundCategory.objects.all()
    shops = Shop.objects.all()
    context = {
        'title': 'Наземный транспорт',
        'transports': transports,
        'cats': cats,
        'shops': shops,
    }
    return render(request, 'transport/index.html', context=context)


def air_transport(request):
    return HttpResponse("Воздушный транспорт")


def show_transport(request, transport_slug):
    return HttpResponse(f'{transport_slug}')