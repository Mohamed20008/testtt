from django.db import models
from datetime import datetime
x =[
    ('phone', 'phone'),
    ('computer', 'computer')
]
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    active = models.BooleanField(default=True)
    category = models.CharField(max_length=50,choices=x, default='phone')
    
    def __str__(self):
        return self.name
    class Meta():
        verbose_name= "Product"
        ordering=['name']
        # ordering=['price']
        # ordering=['-price']
class Test (models.Model):
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    created = models.DateTimeField(null=True , default=datetime.now)
1