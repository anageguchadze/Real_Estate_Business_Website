from django.db import models


class Achievement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Step(models.Model):
    step_number = models.CharField(max_length=30)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"
