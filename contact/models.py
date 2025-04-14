from django.db import models

class InquiryType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class HeardFrom(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class OfficeType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    inquiry_type = models.ForeignKey(InquiryType, on_delete=models.CASCADE, blank=True, null=True)
    heard_about = models.ForeignKey(HeardFrom, on_delete=models.CASCADE, blank=True, null=True)
    message = models.TextField()
    agree_to_terms = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.inquiry_type}"


class OfficeLocation(models.Model):
    title = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    office_type = models.ForeignKey(OfficeType, on_delete=models.CASCADE, blank=True, null=True)
    google_maps_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.office_type})"
