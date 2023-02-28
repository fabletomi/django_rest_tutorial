from django.db import models

# Create your models here.

class Item(models.Model):
    ItemId = models.IntegerField()
    ItemName = models.CharField(max_length=255)
    Price = models.FloatField()
    Quantity = models.IntegerField()
    Category = models.CharField(max_length=255)

    def __str__(self):
        return self.itemName