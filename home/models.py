from django.db import models


class Testimonial(models.Model):
    #what our clients say
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    testimonial = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    rating = models.PositiveIntegerField(default=5, choices=[(i, str(i)) for i in range(1, 6)]) 

    def __str__(self):
        return f"Testimonial from {self.name} ({self.rating} stars)"


class FAQ(models.Model):
    #Frequently asked questions
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question