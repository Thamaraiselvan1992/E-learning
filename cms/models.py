from unicodedata import category
from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from home.models import Course
# Create your models here.
class Category(models.Model):
    name =models.CharField(max_length=250,unique=True)
    course =models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               related_name='home_course')
    def __str__(self):
        return self.name
class Content(models.Model):
    title =models.CharField(max_length=250,unique=True)
    url =models.CharField(max_length=550,default=None, blank=True, null=True)
    category = models.ForeignKey(Category,
                               on_delete=models.CASCADE,
                               related_name='cms_contents')
    slug=models.SlugField(max_length=250,unique=True)
    body = models.TextField(null=True)

    # def __str__(self):
    #     return self.title

    def get_absolute_url(self):
        return reverse('cms:cms_detail', args=[self.slug])

class Note(models.Model):
    title =models.CharField(max_length=250,unique=True)
    message = models.TextField(null=True)
    color =models.CharField(max_length=250)
    user = models.ForeignKey(User, null=True, blank=True,
    on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Resume(models.Model):
        full_name=models.TextField(null=True)
        address=models.TextField(null=True)
        phone=models.TextField(null=True)
        email=models.TextField(null=True)
        about_you=models.TextField(null=True)
        education=models.TextField(null=True)
        career=models.TextField(null=True)
        job_1_start=models.TextField(null=True)
        job_1_end=models.TextField(null=True)
        job_1_details=models.TextField(null=True)
        job_2_start=models.TextField(null=True)
        job_2_end=models.TextField(null=True)
        job_2_details=models.TextField(null=True)
        job_3_start=models.TextField(null=True)
        job_3_end=models.TextField(null=True)
        job_3_details=models.TextField(null=True)
        references =models.TextField(null=True)
        user = models.ForeignKey(User, null=True, blank=True,
        on_delete=models.CASCADE)
        def __str__(self):
            return self.full_name