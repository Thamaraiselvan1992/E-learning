from django.contrib import admin
from .models import Category,Content,Note
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
admin.site.register(Category)
admin.site.register(Content,PostAdmin)
admin.site.register(Note)