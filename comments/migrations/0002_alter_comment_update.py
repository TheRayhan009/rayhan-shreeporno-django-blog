# Generated by Django 5.0.7 on 2024-08-11 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='UPdate',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
