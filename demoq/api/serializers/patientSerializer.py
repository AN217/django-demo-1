from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField
from api.models.patientModels import PatientModelClass, Diag


class PatientSerializer(ModelSerializer):
    class Meta:
        model = PatientModelClass
        fields = '__all__'


class DiagSerializer(ModelSerializer):
    name = CharField(max_length='10')
    patient = PatientSerializer(required=False)
    no_in = SerializerMethodField()

    class Meta:
        model = Diag
        fields = ('name', 'patient', 'id', 'no_in')

    def get_no_in(self, obj):
        return 10
