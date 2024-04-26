from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.title

class Product(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=255)
    price=models.IntegerField()
    stock=models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image=models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.title