from rest_framework.viewsets import ModelViewSet
from api.serializers.patientSerializer import DiagSerializer, Diag
from rest_framework.pagination import PageNumberPagination


class DiagModelViewSet(ModelViewSet):
    """
    retrieve:
    Return the given Diagnosis.

    list:
    Return a list of all the existing Diagnosis.

    create:
    Create a new Diagnosis instance.

    delete:
    Delete a Diagnosis instance.

    update:
    Update a Diagnosis instance.
    """
    serializer_class = DiagSerializer
    queryset = Diag.objects.all()
    pagination_class = PageNumberPagination
