from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Estatein API",
      default_version='v1',
      description="Real Estate API documentation",
      terms_of_service="https://www.estatein.com/terms/",
      contact=openapi.Contact(email="contact@estatein.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('property/', include('property.urls')),
    path('home/', include('home.urls')),
    path('about/', include('about.urls')),
    path('services/', include('services.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
