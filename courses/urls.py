from django.urls import path
from courses.views import devops_questions

urlpatterns = [
    # ... existing paths
    path('devops-learning/', devops_questions, name='devops_learning'),
]
