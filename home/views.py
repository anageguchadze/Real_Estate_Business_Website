from rest_framework import viewsets
from .models import Testimonial, FAQ
from .serializers import TestimonalSerializer, FAQSerializer


class TestimonalViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonalSerializer


class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer