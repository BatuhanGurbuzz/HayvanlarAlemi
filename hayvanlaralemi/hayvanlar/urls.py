from django.urls import path
from hayvanlar.views import index
urlpatterns = [
    path('', index, name = 'index'),
]