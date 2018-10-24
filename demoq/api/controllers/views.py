from rest_framework.viewsets import ModelViewSet
from api.serializers.patientSerializer import DiagSerializer, Diag
from rest_framework.pagination import PageNumberPagination


class DiagModelViewSet(ModelViewSet):
    serializer_class = DiagSerializer
    queryset = Diag.objects.all()
    pagination_class = PageNumberPagination
