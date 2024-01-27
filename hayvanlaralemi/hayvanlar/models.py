from django.db import models
from django.utils.text import slugify
# Create your models here.
class AbstracModel(models.Model):
    updatedDate = models.DateField(
        blank = True,
        auto_now = True,
        verbose_name = 'Updated Date',
        help_text = ''
    )
    
    createdDate = models.DateField(
        blank = True,
        auto_now_add = True,
        null = True,
        verbose_name = 'Created Date',
        help_text = ''
    )
    
    class Meta:
        abstract = True
        
class GeneralSetting(AbstracModel):
    name = models.CharField(
        default = '',
        max_length = 255,
        blank = True,
        verbose_name = 'Genel Ayar Adı',
        help_text = 'Sayfalarda değiştirilmesi istenen alanların ayarlarının adı buradan yapılır.'
    )
    
    description = models.CharField(
        default = '',
        max_length = 255,
        blank = True,
        verbose_name = 'Genel Ayar Adı',
        help_text = 'Kullanılacak yerin neresi olduğuna dair açıklama'
    )
    
    parameter = models.CharField(
        default = '',
        max_length = 255,
        blank = True,
        verbose_name = 'Parametre',
        help_text = 'Kullanılacak yerin alacağı parametre adı'
    )
    
    def __str__(self):
        return f"Genel Ayar: {self.name}"
    
    class Meta:
        verbose_name = 'Genel Ayar'
        
        verbose_name_plural = 'Genel Ayarlar'
        
        ordering = ('name',)
        
class AnimalClass(AbstracModel):
    name = models.CharField(
        default = '',
        max_length = 255,
        null = False,
        verbose_name = 'Hayvan Sınıfı Adı',
    )
    
    slug = models.SlugField(
        null = True,
        unique = True,
        db_index = True,
    )
    
    def __str__(self):
        return f"Sınıf: {self.name}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Hayvan Sınıfı'
        
        verbose_name_plural = 'Hayvan Sınıfları'
        
        ordering = ('name',)
        
    
    
class Animal(AbstracModel):
    name = models.CharField(
        max_length = 255,
        null = False,
        verbose_name = 'Hayvan Adı',
    )
    
    animalClass = models.ForeignKey(AnimalClass, on_delete = models.CASCADE)
    
    description = models.TextField(
        verbose_name = 'Hayvan Açıklaması',
        null = True,
        max_length = 255,
    )
    
    
    slug = models.SlugField(
        null = False,
        unique = True,
        db_index = True,
    )
    
    img = models.ImageField(
        upload_to = 'animals',
        null = True,
        verbose_name = 'Hayvan Resmi',
    )
    
    def __str__(self):
        return f"Hayvan: {self.name}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    
        
    class Meta:
        verbose_name = 'Hayvan'
       
        verbose_name_plural = 'Hayvanlar'
        
        ordering = ('name',)
    
    