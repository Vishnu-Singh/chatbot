from django.contrib import admin
from .models import AnswersPattern,QuestionPattern,Intent
# Register your models here.
admin.site.register(AnswersPattern)
admin.site.register(QuestionPattern)
admin.site.register(Intent)