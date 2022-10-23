from django.conf.urls.static import static
from django.urls import path

from transportgtaonline import settings
from .views import index, show_transport, show_ground_transport, show_air_transport, show_water_transport

urlpatterns = [
    path('', index, name='home'),
    path('transport/<slug:transport_slug>/', show_transport, name='transport'),
    path('ground_transport/', show_ground_transport, name='ground_transport'),
    path('air_transport/', show_air_transport, name='air_transport'),
    path('water_transport/', show_water_transport, name='water_transport'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
