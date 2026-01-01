from django.db import db

class DevOpsQuestion(db.Model):
    title = db.CharField(max_length=200)
    answer = db.TextField()
    category = db.CharField(max_length=100, default="DevOps")

    def __str__(self):
        return self.title
