from django.shortcuts import render, get_object_or_404
from hayvanlar.models import Animal
from django.core.paginator import Paginator
from hayvanlar.api.serializers import AnimalSerializer
from rest_framework import generics
from hayvanlar.api.pagination import SmallPagination

def index(request):
    latest_animals = Animal.objects.all().order_by('-createdDate')[:3]
    
    context = {
        'latest_animals': latest_animals,
    }
    
    return render(request, 'index.html', context)

def animals(request):
    animals = Animal.objects.all()
    page = Paginator(animals, 3)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    
    context = {
        'page': page,
    }
    
    return render(request, 'hayvanlar.html', context)

def animal_details(request, slug):
    animal = get_object_or_404(Animal, slug=slug)
    context = {
        'animals': animal,
    }
    
    return render(request, 'hayvan.html', context)

class AnimalListCreateAPIView(generics.ListCreateAPIView):
    queryset = Animal.objects.all().order_by('-id')
    serializer_class = AnimalSerializer
    pagination_class = SmallPagination
    
class AnimalDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    
    
    




