from django.db import models
from common.models import BaseModel

# Create a products model
class Product(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # sale price property
    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    # get discount
    def get_discount(self):
        return "%.2f" % (float(self.price) * 0.8)


    def __str__(self):
        return self.name
