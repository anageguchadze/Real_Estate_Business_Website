from django.db import models
from django.core.mail import send_mail


class PropertyType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Property(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True, related_name="properties")
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    size = models.PositiveIntegerField(help_text="Size in square meters")
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=0)
    build_year = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Feature(models.Model):
    #ძირითადი მახასიათებლები და კეთილმოწყობა
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="features")
    short_description = models.CharField(max_length=255)

    def __str__(self):
        return self.short_description

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name="images", on_delete=models.CASCADE)
    image = models.TextField()
    def __str__(self):
        return f"Image for {self.property.title}"


class Inquiry(models.Model):
    #მომხმარებლის მიერ შესავსები ველები
    CONTACT_METHODS = [
        ('phone', 'Phone'),
        ('email', 'Email'),
    ]

    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="inquiries")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    preferred_location = models.CharField(max_length=255)
    property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True, related_name="inquiries")
    bedrooms = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=0)
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    contact_method = models.CharField(max_length=10, choices=CONTACT_METHODS)
    message = models.TextField(blank=True, null=True)


    # def send_inquiry_email(self):
    #     if not self.email:
    #         return
        
    #     subject = 'Message confirmation'
    #     message = f'Hello {self.first_name} {self.last_name}, we have received your message.\n\nA company representative will contact you. \n\nThank you!'
    #     send_mail(subject,message,'anamr6211@gmail.com',[self.email],fail_silently=False)


    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     self.send_inquiry_email()

    def __str__(self):
        return f"Inquiry from {self.first_name} {self.last_name} for {self.property.title}"
