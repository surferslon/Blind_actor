from django.db import models


class RandomModel0(models.Model):
    field_0 = models.IntegerField(default=0, null=True, blank=True)
    field_1 = models.CharField(max_length=20, default='', null=True, blank=True)


class RandomModel1(models.Model):
    field_0 = models.CharField(max_length=20, default='', null=True, blank=True)
    field_1 = models.IntegerField(default=0, null=True, blank=True)
