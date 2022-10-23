from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count

from .models import Ground, GroundCategory, Shop, Air, Water


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
    cats = Ground.objects.values('cats__name').annotate(total=Count('id'))
    shops = Ground.objects.values('shops__name').annotate(total=Count('id'))
    context = {
        'title': 'Наземный транспорт',
        'transports': transports,
        'cats': cats,
        'shops': shops,
    }
    return render(request, 'transport/index.html', context=context)


def show_air_transport(request):
    transports = Air.objects.all()
    cats = Air.objects.values('cat__name').annotate(total=Count('id'))
    shops = Air.objects.values('shop__name').annotate(total=Count('id'))
    context = {
        'title': 'Воздушный транспорт',
        'transports': transports,
        'cats': cats,
        'shops': shops,
    }
    return render(request, 'transport/index.html', context=context)


def show_water_transport(request):
    transports = Water.objects.all()
    cats = Water.objects.values('cat__name').annotate(total=Count('id'))
    shops = Water.objects.values('shop__name').annotate(total=Count('id'))
    context = {
        'title': 'Водный транспорт',
        'transports': transports,
        'cats': cats,
        'shops': shops,
    }
    return render(request, 'transport/index.html', context=context)


def show_transport(request, transport_slug):
    return HttpResponse(f'{transport_slug}')