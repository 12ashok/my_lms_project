from django.db import models

class DevOpsTool(models.Model):
    name = models.CharField(max_length=100) # e.g., "Terraform"
    description = models.TextField()
    category = models.CharField(max_length=100) # e.g., "IaC"

    def __str__(self):
        return self.name

class ToolQuestion(models.Model):
    tool = models.ForeignKey(DevOpsTool, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return f"{self.tool.name}: {self.question}"
