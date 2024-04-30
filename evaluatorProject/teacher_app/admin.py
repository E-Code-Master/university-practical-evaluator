from django.contrib import admin
from .models import Question, QuestionBank, QuestionPaper, AnswerSheet

# Register your models here.
admin.site.register(Question)
admin.site.register(QuestionBank)
admin.site.register(QuestionPaper)
admin.site.register(AnswerSheet)