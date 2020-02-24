# Generated by Django 3.0.3 on 2020-02-24 18:32

from django.db import migrations
from app1.models import RandomModel0, RandomModel1


def forwards(apps, schema_editor):
    RandomModel0.objects.get_or_create(field_0=123, field_1='asdf')
    RandomModel0.objects.get_or_create(field_0=234, field_1='qwer')
    RandomModel0.objects.get_or_create(field_0=897, field_1='xzcv')
    RandomModel0.objects.get_or_create(field_0=234, field_1='poiu')
    RandomModel0.objects.get_or_create(field_0=987, field_1=';lkj')
    RandomModel0.objects.get_or_create(field_0=452, field_1='poiu')
    RandomModel0.objects.get_or_create(field_0=999, field_1='juiop')
    RandomModel1.objects.get_or_create(field_1=897, field_0='xzcv')
    RandomModel1.objects.get_or_create(field_1=234, field_0='poiu')
    RandomModel1.objects.get_or_create(field_1=987, field_0=';lkj')
    RandomModel1.objects.get_or_create(field_1=452, field_0='poiu')
    RandomModel1.objects.get_or_create(field_1=999, field_0='juiop')


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
