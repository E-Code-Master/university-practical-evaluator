from django.db import models
from django.conf import settings
from admin_app.models import Subject, CodingLanguage, Teacher, Student, Course, Semester

class QuestionType(models.TextChoices):
    MCQ = "MCQ", 'Multiple Choice Question'
    PROG = "PROG", 'Program'

class Question(models.Model):
    subject = models.ForeignKey(Subject, blank=True, null=True, on_delete=models.CASCADE, related_name='subject_of_question')
    coding_language = models.CharField(max_length=100, blank=True, null=True, default=CodingLanguage.PYTHON, choices=CodingLanguage.choices)
    type = models.CharField(max_length=30, blank=True, null=True, default=QuestionType.MCQ, choices=QuestionType.choices)
    summary = models.CharField(max_length=400, blank=True, null=True)
    options = models.CharField(max_length=1)
    expected_output = models.CharField(max_length=400, blank=True, null=True)
    weightage = models.FloatField(blank=True, null=True, default=0.5)

    created_at=models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='question_created_by', blank=True, null=True)
    updated_at= models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='question_updated_by', blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.subject}: {self.summary}' 

class QuestionBank(models.Model):
    prepared_by = models.OneToOneField(Teacher, blank=True, null=True, on_delete=models.CASCADE, related_name='question_bank_prepared_by')
    course = models.OneToOneField(Course, blank=True, null=True, on_delete=models.CASCADE, related_name='question_papers_course')
    semester = models.CharField(max_length=100, blank=True, null=True, default=Semester.FIRST, choices=Semester.choices)
    subject = models.OneToOneField(Subject, blank=True, null=True, on_delete=models.CASCADE, related_name='question_papers_subject')
    question = models.ForeignKey(Question, blank=True, null=True, on_delete=models.CASCADE, related_name='question_papers_question')

class QuestionPaper(models.Model):
    title = models.CharField(max_length=400, blank=True, null=True)
    total_marks = models.IntegerField(blank=True, null=True, default=100)
    prepared_by = models.OneToOneField(Teacher, blank=True, null=True, on_delete=models.CASCADE, related_name='question_paper_prepared_by')
    duration = models.IntegerField(blank=True, null=True, default=90)
    exam_datetime = models.DateField() 
    course = models.OneToOneField(Course, blank=True, null=True, on_delete=models.CASCADE, related_name='question_paper_course')
    semester = models.CharField(max_length=100, blank=True, null=True, default=Semester.FIRST, choices=Semester.choices)
    subject = models.OneToOneField(Subject, blank=True, null=True, on_delete=models.CASCADE, related_name='question_paper_subject')
    question = models.ForeignKey(Question, blank=True, null=True, on_delete=models.CASCADE, related_name='question_paper_question')

class AnswerSheet(models.Model):
    student = models.OneToOneField(Student, blank=True, null=True, on_delete=models.CASCADE, related_name='answer_sheet_student')
    question_paper = models.ForeignKey(QuestionPaper, blank=True, null=True, on_delete=models.CASCADE, related_name='answer_sheet_teacher')
    