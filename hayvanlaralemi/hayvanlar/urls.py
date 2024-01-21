from django.urls import path
from hayvanlar.views import index, animals
urlpatterns = [
    path('', index, name = 'anasayfa'),
    path('hayvanlar/', animals, name = 'hayvanlar')
    
]