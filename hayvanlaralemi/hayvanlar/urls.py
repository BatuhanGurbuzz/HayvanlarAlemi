from django.urls import path
from hayvanlar.views import index, animal_details, animals

urlpatterns = [
    path('', index, name='anasayfa'),
    path('hayvanlar/', animals, name='animals'),
    path('hayvanlar/<slug:slug>/', animal_details, name='animals_details'),
]