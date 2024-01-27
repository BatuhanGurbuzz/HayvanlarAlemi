from django.urls import path
from hayvanlar.views import index, animal_details, animals, AnimalListCreateAPIView, AnimalDetailAPIView

urlpatterns = [
    path('', index, name='anasayfa'),
    path('hayvanlar/', animals, name='animals'),
    path('hayvanlar/<slug:slug>/', animal_details, name='animals_details'),
    path('api/hayvanlar/', AnimalListCreateAPIView.as_view(), name='api_animals'),
    path('api/hayvanlar/<int:pk>/', AnimalDetailAPIView.as_view(), name='api_animals_detail')
    
]