from django.db import models
from uuid import uuid4
import os

# Create your models here.
class PickelData(models.Model):
    uuid = models.CharField(primary_key=True,default=uuid4,max_length=50)
    dependent_variables = models.FileField(upload_to="./checkpoints/")
    independent_variables = models.FileField(upload_to="./checkpoints/")
    checkpoint_state = models.FileField(upload_to="./checkpoints/")