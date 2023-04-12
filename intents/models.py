from django.db import models
from uuid import uuid4

# Create your models here.
class QuestionPattern(models.Model):
    uuid = models.CharField(primary_key=True,default=uuid4,max_length=60)
    questions = models.CharField(max_length=50)

class AnswersPattern(models.Model):
    uuid = models.CharField(primary_key=True,default=uuid4,max_length=60)
    answers = models.CharField(max_length=50)

class Intent(models.Model):
    uuid = models.CharField(primary_key=True,default=uuid4,max_length=60)
    question_tag = models.CharField(max_length=50)
    question_pattern = models.ForeignKey(QuestionPattern,verbose_name=("question_pattern"),on_delete=models.DO_NOTHING)
    answer_pattern = models.ForeignKey(AnswersPattern,verbose_name=("answer_pattern"),on_delete=models.DO_NOTHING)