from django.shortcuts import render
from .models import DevOpsQuestion

def devops_questions(request):
    questions = DevOpsQuestion.objects.all()
    return render(request, 'courses/devops_list.html', {'questions': questions})
