from django.db import models


class TestModel(models.Model):
    char_field = models.CharField(max_length=20, default='', null=True, blank=True)
    int_field = models.IntegerField(default=0, blank=True, null=True)
    float_field = models.FloatField(default=0.0, blank=True, null=True)
