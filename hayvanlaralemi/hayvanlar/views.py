from django.shortcuts import render, get_object_or_404
from hayvanlar.models import GeneralSetting, Animal
from django.core.paginator import Paginator

def get_general_setting(parameter):
    try:
        obj = GeneralSetting.objects.get(name=parameter).parameter
    except:
        obj = ''

    return obj

def layout(request):
    # General Settings Start #
    site_title = get_general_setting('site_title')
    site_description = get_general_setting('site_description')
    # General Settings End #
    
    animals = Animal.objects.all()
    
    context = {
        'site_title': site_title,
        'site_description': site_description,
        'animals': animals,
    }
    
    return context

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