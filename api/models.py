from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#producs model with name,price,stock and image fields
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    stock=models.IntegerField()
    image=models.ImageField(upload_to='products',blank=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE, related_name='products', null=True)
    #string representation of the model
    def __str__(self):
        return self.name
