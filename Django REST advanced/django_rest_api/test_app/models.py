from django.db import models

# Create your models here.



class Product(models.Model):
    product_tag = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to="Images", default="2.jpg")

    

    def __str__(self):
        return '{} {}'.format(self.product_tag,self.name)
