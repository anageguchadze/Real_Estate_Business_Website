from rest_framework import viewsets
from .models import ContactMessage, OfficeLocation, InquiryType, HeardFrom, OfficeType
from .serializers import ContactMessageSerializer, OfficeLocationSerializer, InquiryTypeSerializer, HeardFromSerializer, OfficeTypeSerializer


class InquiryTypeViewSet(viewsets.ModelViewSet):
    queryset = InquiryType.objects.all()
    serializer_class = InquiryTypeSerializer


class HeardFromViewSet(viewsets.ModelViewSet):
    queryset = HeardFrom.objects.all()
    serializer_class = HeardFromSerializer


class OfficeTypeViewSet(viewsets.ModelViewSet):
    queryset = OfficeType.objects.all()
    serializer_class = OfficeTypeSerializer


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer


class OfficeLocationViewSet(viewsets.ModelViewSet):
    queryset = OfficeLocation.objects.all()
    serializer_class = OfficeLocationSerializer
