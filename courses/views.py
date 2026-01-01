from django.shortcuts import render, get_object_or_404
from .models import Course, Lesson

def course_list(request):
    # Fetch all courses from the database
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    # Fetch a specific course and its lessons
    course = get_object_or_404(Course, pk=course_id)
    lessons = Lesson.objects.filter(course=course)
    return render(request, 'courses/course_detail.html', {
        'course': course, 
        'lessons': lessons
    })