from django.urls import path

from .views import index, show_transport, show_ground_transport

urlpatterns = [
    path('', index, name='home'),
    path('ground_transport/', show_ground_transport, name='ground_transport'),
    path('transport/<slug:transport_slug>/', show_transport, name='transport'),
]
