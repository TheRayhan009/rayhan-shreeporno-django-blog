# Generated by Django 5.0.7 on 2024-08-14 06:32

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserImages', '0002_alter_upimage_puimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='upimage',
            name='A_imageSlug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='UPtitel', unique=True),
        ),
    ]
