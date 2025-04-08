from rest_framework import viewsets
from .models import SellingService, ManagementService, InvestmentService
from .serializers import SellingServiceSerializer, ManagementServiceSerializer, InvestmentServiceSerializer

class SellingServiceViewSet(viewsets.ModelViewSet):
    queryset = SellingService.objects.all()
    serializer_class = SellingServiceSerializer


class ManagementServiceViewSet(viewsets.ModelViewSet):
    queryset = ManagementService.objects.all()
    serializer_class = ManagementServiceSerializer


class InvestmentServiceViewSet(viewsets.ModelViewSet):
    queryset = InvestmentService.objects.all()
    serializer_class = InvestmentServiceSerializer
