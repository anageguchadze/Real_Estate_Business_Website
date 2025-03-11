from rest_framework import viewsets, filters
from .models import Property, PropertyImage, PropertyType, Inquiry, Feature
from .serializers import PropertySerializer, PropertyImageSerializer, PropertyTypeSerializer, InquirySerializer, FeatureSerializer
from .filters import PropertyFilter
from django_filters.rest_framework import DjangoFilterBackend


class PropertyTypeViewSet(viewsets.ModelViewSet):
    queryset = PropertyType.objects.all()   
    serializer_class = PropertyTypeSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Assign filter class for advanced filtering
    filterset_class = PropertyFilter

    # Enable search on location and property type name
    search_fields = ['location', 'property_type__name', 'price', 'size', 'build_year']  # Ensure property_type.name exists

    # # Enable ordering by price, size, and build year
    # ordering_fields = ['price', 'size', 'build_year']
    # ordering = ['price']  # Default ordering by price


class PropertyImageViewSet(viewsets.ModelViewSet):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer


class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer