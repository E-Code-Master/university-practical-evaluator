from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils import timezone
from django.conf import settings

class Role(models.TextChoices):
    ADMIN = "ADMIN", 'Admin'
    STUDENT = "STUDENT", 'Student'
    TEACHER = "TEACHER", 'Teacher'

class CodingLanguage(models.TextChoices):
    PYTHON = "PYTHON", 'Python'
    JAVA = "JAVA", 'Java'

class Semester(models.TextChoices):
    FIRST = "FIRST", 'First'
    SECOND = "SECOND", 'Second'
    THIRD = "THIRD", 'Third'
    FOURTH = "FOURTH", 'Fourth'
    FIFTH = "FIFTH", 'Fifth'
    SIXTH = "SIXTH", 'Sixth'
    SEVENTH = "SEVENTH", 'Seventh'
    EIGHTH = "EIGHTH", 'Eighth'
    NINTH = "NINTH", 'Ninth'
    TENTH = "TENTH", 'Tenth'

class Address(models.Model):
    name = models.CharField(max_length=400, blank=True, null=True)
    address_one = models.CharField(max_length=300)
    address_two = models.CharField(max_length=300)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()

    created_at=models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='address_created_by', blank=True, null=True)
    updated_at= models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='address_updated_by', blank=True, null=True)

    def get_full_address(self) -> str:
        """
        Return the full address with a space in between.
        """
        full_address = '%s %s %s %s' % (self.address_one, self.address_two, self.city, self.state)
        return full_address.strip()
    
    def __str__(self) -> str:
        return self.get_full_address()
    
    def save(self, *args, **kwargs):
        super().save()

class University(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    head_office_address = models.ForeignKey(Address, blank=True, null=True, on_delete=models.CASCADE, related_name='university_address')
    is_deemed = models.BooleanField()

    created_at=models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='university_created_by', blank=True, null=True)
    updated_at= models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='university_updated_by', blank=True, null=True)


    def __str__(self) -> str:
        return self.name

class College(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    university = models.OneToOneField(University, blank=True, null=True, on_delete=models.CASCADE, related_name='university')
    address = models.OneToOneField(Address, blank=True, null=True, on_delete=models.CASCADE, related_name='college_address')

    created_at=models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='college_created_by', blank=True, null=True)
    updated_at= models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='college_updated_by', blank=True, null=True)


    def __str__(self) -> str:
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    college = models.OneToOneField(College, blank=True, null=True, on_delete=models.CASCADE, related_name='college_of_this_department')

    created_at=models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='department_created_by', blank=True, null=True)
    updated_at= models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='department_updated_by', blank=True, null=True)


    def __str__(self) -> str:
        return self.name

class Course(models.Model):

    name = models.CharField(max_length=300, blank=True, null=True)
    code = models.IntegerField()
    department = models.OneToOneField(Department, blank=True, null=True, on_delete=models.CASCADE, related_name='course_department')

    created_at=models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='course_created_by', blank=True, null=True)
    updated_at= models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='course_updated_by', blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    code = models.IntegerField()
    course = models.OneToOneField(Course, blank=True, null=True, on_delete=models.CASCADE, related_name='íts_course')

    created_at=models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='subject_created_by', blank=True, null=True)
    updated_at= models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='subject_updated_by', blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class User(AbstractUser):
    base_role = Role.ADMIN
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    contact = models.CharField(max_length=10, validators=[RegexValidator(regex='^.{10}$', message='Contact number must be 10 digits')])
    permanent_address = models.ForeignKey(Address, blank=True, null=True, on_delete=models.CASCADE, related_name='permanent_address_of_student')
    pan_number = models.CharField(blank=True, null=True, validators=[RegexValidator(regex='^.{10}$', message='PAN Card number must be 10 characters long.', code='nomatch')])
    aadhar_number = models.CharField(blank=True, null=True, validators=[RegexValidator(regex='^.{12}$', message='PAN Card number must be 12 characters long.', code='nomatch')])
    role = models.CharField(max_length=20, default=base_role, choices=Role.choices)

    created_at=models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='user_created_by', blank=True, null=True)
    updated_at= models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='user_updated_by', blank=True, null=True)


    def __str__(self) -> str:
        return self.username

class AdminUser(models.Model):
    base_role = Role.ADMIN

    def __str__(self) -> str:
        return self.get_full_name()

class Teacher(User):
    base_role = Role.TEACHER

    def __str__(self) -> str:
        return self.get_full_name()

class Student(models.Model):
    base_role = Role.STUDENT
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE, related_name='user')
    fathers_name = models.CharField(max_length=30)
    college = models.ForeignKey(College, blank=True, null=True, on_delete=models.CASCADE, related_name='student_college')
    department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.CASCADE, related_name='student_department')
    course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.CASCADE, related_name='student_course')
    semister = models.CharField(max_length=100, blank=True, null=True, choices=Semester.choices)
    roll_no = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.get_full_name()
    
class ScheduleExam(models.Model):
    college = models.OneToOneField(College, blank=True, null=True, on_delete=models.CASCADE, related_name='schedule_exam_college')
    department = models.OneToOneField(College, blank=True, null=True, on_delete=models.CASCADE, related_name='schedule_exam_department')
    exam_datetime = models.DateField()

    created_at=models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='schedule_exam_created_by', blank=True, null=True)
    updated_at= models.DateField(auto_now_add=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name='schedule_exam_updated_by', blank=True, null=True)

    def __str__(self) -> str:
        return self.exam_datetime