from rest_framework import viewsets, filters
from .models import Property, PropertyImage, PropertyType, Inquiry, Feature
from .serializers import PropertySerializer, PropertyImageSerializer, PropertyTypeSerializer, InquirySerializer, FeatureSerializer
from .filters import PropertyFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class PropertyTypeViewSet(viewsets.ModelViewSet):
    queryset = PropertyType.objects.all()   
    serializer_class = PropertyTypeSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filterset_class = PropertyFilter
    search_fields = ["location", "property_type__name"]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
   
    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('search', openapi.IN_QUERY, description="Search by location or property type", type=openapi.TYPE_STRING),
        openapi.Parameter('location', openapi.IN_QUERY, description="Exact location", type=openapi.TYPE_STRING),
        openapi.Parameter('property_type', openapi.IN_QUERY, description="Exact property type", type=openapi.TYPE_STRING),
        openapi.Parameter('build_year', openapi.IN_QUERY, description="Year the property was built", type=openapi.TYPE_INTEGER),
        openapi.Parameter('min_price', openapi.IN_QUERY, description="Minimum price", type=openapi.TYPE_INTEGER),
        openapi.Parameter('max_price', openapi.IN_QUERY, description="Maximum price", type=openapi.TYPE_INTEGER),
        openapi.Parameter('price_range', openapi.IN_QUERY, description="Custom price range like '100000-300000' or '500000+'", type=openapi.TYPE_STRING),
        openapi.Parameter('min_size', openapi.IN_QUERY, description="Minimum size", type=openapi.TYPE_INTEGER),
        openapi.Parameter('max_size', openapi.IN_QUERY, description="Maximum size", type=openapi.TYPE_INTEGER),
        openapi.Parameter('size_range', openapi.IN_QUERY, description="Custom size range like '100-200' or '500+'", type=openapi.TYPE_STRING),
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

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


