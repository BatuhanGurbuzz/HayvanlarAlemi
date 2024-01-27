from django.contrib import admin
from hayvanlar.models import GeneralSetting, Animal, AnimalClass
# Register your models here.

@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter', 'updatedDate', 'createdDate']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']
    
    class Meta:
        model = GeneralSetting
        
@admin.register(AnimalClass)
class AnimalClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'updatedDate', 'createdDate']
    search_fields = ['name']
    list_editable = ['name']
    readonly_fields = ['slug']
    class Meta:
        model = AnimalClass
        
@admin.register(Animal) 
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'animalClass', 'img', 'slug', 'description', 'updatedDate', 'createdDate']
    search_fields = ['name', 'slug', 'animalClass']
    list_editable = ['name', 'description']
    readonly_fields = ['slug']
    
    class Meta:
        model = Animal