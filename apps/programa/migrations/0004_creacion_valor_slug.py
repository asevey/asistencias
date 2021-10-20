# Generated by Django 3.1 on 2021-10-20 22:36

from django.db import migrations
from django.utils.text import slugify


def crear_slug_en_programas_existentes(apps, schemas):
    Programa = apps.get_model('programa', 'Programa')
    for programa in Programa.objects.all():
        programa.slug = slugify(programa.nombre)
        programa.save()


class Migration(migrations.Migration):

    dependencies = [
        ('programa', '0003_programa_slug'),
    ]

    operations = [
        migrations.RunPython(crear_slug_en_programas_existentes,
                             reverse_code=migrations.RunPython.noop)
    ]
