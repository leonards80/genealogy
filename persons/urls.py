from django.conf.urls import url
from django.urls import path
from .views import (
    persons_list,
    persons_details,
    )

urlpatterns = [
    url(r'^$', persons_list, name='persons_list'),
    url(r'^details$', persons_details, name='persons_details'),
]
