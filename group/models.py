from django.db import models
from auth_system.models import CustomUser
# Create your models here.




class Group(models.Model):
    name = models.CharField(max_length=50)
    class_teacher = models.ForeignKey(CustomUser, related_name="class_teacher", on_delete=models.DO_NOTHING, default=None)
    students = models.ManyToManyField(CustomUser, related_name="students")

    def __str__(self):
        return self.name

