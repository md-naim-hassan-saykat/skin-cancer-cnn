# Generated by Django 4.0.4 on 2022-05-09 23:18

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_skincancer_akiec_alter_skincancer_bcc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skincancer',
            name='image',
            field=models.ImageField(upload_to=core.models.upload_to),
        ),
    ]
