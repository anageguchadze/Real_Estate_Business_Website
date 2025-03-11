import django_filters
from .models import Property

class PropertyFilter(django_filters.FilterSet):
    # Filter by exact location (from available locations)
    location = django_filters.CharFilter(field_name="location", lookup_expr="iexact", label="Location")

    # Filter by property type (exact match from predefined types)
    property_type = django_filters.CharFilter(field_name="property_type__name", lookup_expr="iexact", label="Property Type")

    # Filter by price range (exact match based on our dynamic ranges)
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte", label="Minimum Price")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte", label="Maximum Price")

    # Filter by property size
    min_size = django_filters.NumberFilter(field_name="size", lookup_expr="gte", label="Minimum Size")
    max_size = django_filters.NumberFilter(field_name="size", lookup_expr="lte", label="Maximum Size")

    # Filter by build year
    min_build_year = django_filters.NumberFilter(field_name="build_year", lookup_expr="gte", label="Minimum Build Year")
    max_build_year = django_filters.NumberFilter(field_name="build_year", lookup_expr="lte", label="Maximum Build Year")

    class Meta:
        model = Property
        fields = ["location", "property_type", "min_price", "max_price", "min_size", "max_size", "min_build_year", "max_build_year"]
