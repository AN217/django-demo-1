from django.db import models


# Create your models here.
class BaseClass(models.Model):
    """
    @summary :- This is the base class which every model class should implement
    @author :- Anshul Gupta
    @:param :-author
    """
    author = models.CharField(help_text="who is adding this record", max_length=100)


class PatientModelClass(BaseClass):
    first_name = models.CharField(help_text="Patients First name", max_length=100)


class Diag(BaseClass):
    name = models.CharField(help_text="some data", max_length=100)
    patient = models.ForeignKey(PatientModelClass, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'patient')
