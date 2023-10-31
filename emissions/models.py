from django.db import models

# Emissions Modal to represent the data

class Emissions(models.Model):
    id = models.IntegerField(primary_key=True)
    date_created = models.DateTimeField("date_created")
    accounting_period = models.CharField(max_length=400)
    scope_1 = models.IntegerField(null=True)
    scope_2 = models.IntegerField(null=True)
    scope_3 = models.IntegerField(null=True)

