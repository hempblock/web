# Generated by Django 2.0.5 on 2018-05-28 19:18

from django.db import migrations


def forwards_func(apps, schema_editor):
    EmailEvent = apps.get_model('marketing', 'EmailEvent')
    for ee in EmailEvent.objects.all():
        if not ee.ip_address:
            ee.ip_address = ee.payload.get('ip')
            ee.save()
            print(ee.pk)


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0026_emailevent_ip_address'),
    ]

    operations = [
        migrations.RunPython(
            forwards_func,
        ),
    ]