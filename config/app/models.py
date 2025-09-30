from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Car(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField(validators=[MinValueValidator(1885), MaxValueValidator(2025)])
    color = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name