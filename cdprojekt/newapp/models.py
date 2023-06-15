from django.db import models


# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=50)
    date = models.IntegerField()
    color = models.CharField(max_length=50)
    mileage = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.brand} - {self.date} - {self.color} - {self.mileage} - {self.price}"
