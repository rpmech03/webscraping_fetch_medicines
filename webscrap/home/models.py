from django.db import models
import uuid

class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    crerated_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True

class Stocks(BaseModel):
    stock_name = models.CharField(max_length=100)
    stock_url = models.URLField()


#Abstract Base Class :-

# Abstract Base Class are useful when you want to put some common information into a number of other models. 
# You write your base class and put abstract = True in the Meta Class. Suppose you have two model Student and Teacher.