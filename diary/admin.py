from django.contrib import admin
from .models import Teacher, Student, Subject, Mark, Diary
# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Diary)
admin.site.register(Mark)

