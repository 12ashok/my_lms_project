from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='course_logos/')
    created_at = models.DateTimeField(auto_now_add=True)

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_index=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video_url = models.URLField()  # Link to YouTube/Vimeo
    content = models.TextField()   # Text instructions