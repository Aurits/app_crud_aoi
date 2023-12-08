from django.db import models

# Create your models here.
#producs model with name,price,stock and image fields
class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=7,decimal_places=2)
    stock=models.IntegerField()
    image=models.ImageField(upload_to='products',blank=True)
    #string representation of the model
    def __str__(self):
        return self.name
