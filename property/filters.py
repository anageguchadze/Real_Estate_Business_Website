import django_filters
from .models import Property, PropertyType

class PropertyFilter(django_filters.FilterSet):
    # Filter by location
    location = django_filters.CharFilter(lookup_expr='icontains', label="Location")

    # Filter by property type
    property_type = django_filters.ModelChoiceFilter(queryset=PropertyType.objects.all(), label="Property Type")

    # Filter by price range
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label="Minimum Price")
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label="Maximum Price")

    # Filter by property size (square meters)
    min_size = django_filters.NumberFilter(field_name='size', lookup_expr='gte', label="Minimum Size")
    max_size = django_filters.NumberFilter(field_name='size', lookup_expr='lte', label="Maximum Size")

    # Filter by build year
    min_build_year = django_filters.NumberFilter(field_name='build_year', lookup_expr='gte', label="Minimum Build Year")
    max_build_year = django_filters.NumberFilter(field_name='build_year', lookup_expr='lte', label="Maximum Build Year")

    class Meta:
        model = Property
        fields = ['location', 'property_type', 'min_price', 'max_price', 'min_size', 'max_size', 'min_build_year', 'max_build_year']
