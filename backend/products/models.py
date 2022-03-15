from django.db import models

# Create a products model
class Product(models.Model):
    # Create a name field
    name = models.CharField(max_length=200)
    # Create a description field
    description = models.TextField(blank=True, null=True)
    # Create a price field
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # Create a date_created field
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
