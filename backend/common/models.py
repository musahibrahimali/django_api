from xmlrpc.client import DateTime
from django.db import models

# Create a base models for other models to inherit from
class BaseModel(models.Model):
    '''
        BaseModel
        an abstract base model with the most common fields 
        all the models may have in common
    '''
    # create at field with today's date and time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
