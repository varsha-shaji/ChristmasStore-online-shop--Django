from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)

class Cart(models.Model):
    user=models.ForeignKey(Register,on_delete=models.CASCADE)
    product=models.ForeignKey('administrator.Product',on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    def __str__(self):
        return self.product.title