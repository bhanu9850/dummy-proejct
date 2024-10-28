from django.db import models

class NewModel(models.Model):
    field_one = models.CharField(max_length=100)
    field_two = models.IntegerField()
    field_three = models.DateField()
    field_four = models.BooleanField(default=False)
