from django.db import models
from uuid import uuid4
# Create your models here.
class PickelData(models.Model):
    uuid = models.CharField(primary_key=True,default=uuid4,max_length=50)
    dependent_variables = models.BinaryField()
    independent_variables = models.BinaryField()
    checkpoint_state = models.BinaryField()