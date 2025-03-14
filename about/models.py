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


class Staff(models.Model):
    image = models.TextField()
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Clients(models.Model):
    year = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.company_name