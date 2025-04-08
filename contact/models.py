from django.db import models

INQUIRY_CHOICES = [
    ('buying', 'Buying'),
    ('selling', 'Selling'),
    ('investment', 'Investment'),
    ('other', 'Other'),
]

HEARD_FROM_CHOICES = [
    ('google', 'Google'),
    ('social_media', 'Social Media'),
    ('referral', 'Referral'),
    ('other', 'Other'),
]

OFFICE_TYPE_CHOICES = [
    ('headquarters', 'Headquarters'),
    ('regional', 'Regional Office'),
    ('international', 'International Office'),
]


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    inquiry_type = models.CharField(max_length=50, choices=INQUIRY_CHOICES)
    heard_about = models.CharField(max_length=50, choices=HEARD_FROM_CHOICES)
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
    office_type = models.CharField(max_length=50, choices=OFFICE_TYPE_CHOICES)
    google_maps_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.office_type})"
