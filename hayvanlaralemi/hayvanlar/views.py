from django.shortcuts import render
from hayvanlar.models import GeneralSetting, Animal
# Create your views here.

def get_general_setting(parameter):
    try:
        obj = GeneralSetting.objects.get(name=parameter).parameter
    except:
        obj = ''

    return obj

def layout(request):
    
    context = {}
    
    return context


def index(request):
    return render(request, 'index.html')

def animals(request):
    return render(request, 'hayvanlar.html')