from django.contrib import admin
# Register your models here.
from .models import Address, University, College, Department, Course, Subject, User, AdminUser, Teacher, Student, ScheduleExam


# Register your models here.
admin.site.register(Address)
admin.site.register(University)
admin.site.register(College)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(User)
admin.site.register(AdminUser)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(ScheduleExam)