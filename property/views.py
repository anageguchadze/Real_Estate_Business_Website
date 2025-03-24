from rest_framework import viewsets, filters
from .models import Property, PropertyImage, PropertyType, Inquiry, Feature
from .serializers import PropertySerializer, PropertyImageSerializer, PropertyTypeSerializer, InquirySerializer, FeatureSerializer
from .filters import PropertyFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView


class PropertyTypeViewSet(viewsets.ModelViewSet):
    queryset = PropertyType.objects.all()   
    serializer_class = PropertyTypeSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PropertyFilter
    search_fields = ["location", "property_type__name"]
   

    def get_queryset(self):
        return Property.objects.all().distinct()


class PropertyFilterOptionsView(APIView):
    def get(self, request):
        # Get unique locations
        locations = list(Property.objects.values_list('location', flat=True).distinct())

        # Get unique property types
        property_types = list(PropertyType.objects.values_list('name', flat=True).distinct())

        # Get distinct build years, ignoring NULL values
        build_years = sorted(filter(None, Property.objects.values_list('build_year', flat=True).distinct()))

        # Define price ranges manually
        price_ranges = [
            "$0 - $50,000",
            "$50,000 - $100,000",
            "$100,000 - $500,000",
            "$500,000 - $1,000,000",
            "$1,000,000+"
        ]

        # Define property size ranges
        size_ranges = [
            "0 - 50 sqm",
            "50 - 100 sqm",
            "100 - 200 sqm",
            "200 - 500 sqm",
            "500+ sqm"
        ]

        return Response({
            "locations": locations,
            "property_types": property_types,
            "build_years": build_years,
            "price_ranges": price_ranges,
            "size_ranges": size_ranges,
        })


class PropertyImageViewSet(viewsets.ModelViewSet):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer


class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    pagination_class = None

class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


