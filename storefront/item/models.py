from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price=models.FloatField()
    quantity=models.IntegerField(blank=True, null=True)
    img=models.ImageField(upload_to='itemImages', blank=True, null=True)
    isSold = models.BooleanField(default=False)
    isSale = models.BooleanField(default=False)
    isNew = models.BooleanField(default=False)
    isBestseller = models.BooleanField(default=False)
    createdBy = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

