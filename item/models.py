from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=255)
  
  def __str__(self):
    return self.name
  
  class Meta:
    ordering = ('name', )
    
    verbose_name = 'category'
    verbose_name_plural = 'categories'
    
    
class Item(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True)
 