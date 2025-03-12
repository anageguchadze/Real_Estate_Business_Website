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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = PropertyFilter
    search_fields = ["location", "property_type__name"]
    ordering_fields = ["price", "size", "build_year"]
    ordering = ["price"]
    ordering = ["build_year"]

    def get_queryset(self):
        return Property.objects.all().distinct()


class PropertyFilterOptionsView(APIView):
    def get(self, request):
        # Get unique locations
        locations = list(Property.objects.values_list('location', flat=True).distinct())

        # Get unique property types
        property_types = list(PropertyType.objects.values_list('name', flat=True).distinct())

        # Get price ranges (modify as needed)
        price_values = list(Property.objects.values_list('price', flat=True).distinct())
        price_ranges = sorted(set([f"${int(price)} - ${int(price) + 50000}" for price in price_values]))

        # Get property sizes
        sizes = list(Property.objects.values_list('size', flat=True).distinct())

        # Get build years
        build_years = list(Property.objects.values_list('build_year', flat=True).distinct())

        return Response({
            "locations": locations,
            "property_types": property_types,
            "pricing_ranges": price_ranges,
            "property_sizes": sizes,
            "build_years": build_years,
        })


class PropertyImageViewSet(viewsets.ModelViewSet):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer


class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer