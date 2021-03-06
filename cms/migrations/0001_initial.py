# Generated by Django 4.0.3 on 2022-03-25 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_course', to='home.course')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(null=True)),
                ('address', models.TextField(null=True)),
                ('phone', models.TextField(null=True)),
                ('email', models.TextField(null=True)),
                ('about_you', models.TextField(null=True)),
                ('education', models.TextField(null=True)),
                ('career', models.TextField(null=True)),
                ('job_1_start', models.TextField(null=True)),
                ('job_1_end', models.TextField(null=True)),
                ('job_1_details', models.TextField(null=True)),
                ('job_2_start', models.TextField(null=True)),
                ('job_2_end', models.TextField(null=True)),
                ('job_2_details', models.TextField(null=True)),
                ('job_3_start', models.TextField(null=True)),
                ('job_3_end', models.TextField(null=True)),
                ('job_3_details', models.TextField(null=True)),
                ('references', models.TextField(null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('message', models.TextField(null=True)),
                ('color', models.CharField(max_length=250)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('url', models.CharField(blank=True, default=None, max_length=550, null=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('body', models.TextField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cms_contents', to='cms.category')),
            ],
        ),
    ]
