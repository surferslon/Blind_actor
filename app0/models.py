from django.db import models


class RandomModel0(models.Model):
    int_field = models.IntegerField(blank=True, null=True, default=0)
    float_field = models.FloatField(blank=True, null=True, default=0.0)
    char_field = models.CharField(max_length=255, blank=True, null=True, default='')


class RandomModel1(models.Model):
    char_field = models.CharField(max_length=20, blank=True, null=True, default='')
    fk_field = models.ForeignKey(RandomModel0, on_delete=models.CASCADE, default=None, null=True, blank=True)
