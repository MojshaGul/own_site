from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
        categories = [
              (1,"technik"),
              (2,"toys"),
              (3,"food")
        ]
        name = models.CharField(max_length=100)  
        price = models.DecimalField(max_digits=10, decimal_places=2) 
        description = models.TextField(blank=True) 
        created_at = models.DateTimeField(auto_now_add=True) 
        count = models.IntegerField()
        categori = models.IntegerField(choices=categories)

        def __str__(self):
            return self.name
        
class item_cart(models.Model):
      owner = models.ForeignKey(User)
      items_count = models.IntegerField()
      item_id = models.ForeignKey(Product)

