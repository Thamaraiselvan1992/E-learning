from django.db import models

# Create your models here.
class Course(models.Model):
    course_name =models.CharField(max_length=250,unique=True)
    image = models.ImageField(upload_to='images',null=True) 
    def __str__(self):
        return self.course_name