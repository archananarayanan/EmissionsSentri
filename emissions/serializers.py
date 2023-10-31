from emissions.models import Emissions
from rest_framework import serializers


# Emissions Serailizer to read the data from Database 

class EmissionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Emissions
        fields = ['id', 'date_created', 'accounting_period', 'scope_1', 'scope_2','scope_3']