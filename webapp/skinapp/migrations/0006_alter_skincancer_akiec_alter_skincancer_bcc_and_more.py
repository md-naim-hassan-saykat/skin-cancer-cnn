# Generated by Django 4.0.4 on 2022-05-10 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_skincancer_akiec_alter_skincancer_bcc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skincancer',
            name='akiec',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skincancer',
            name='bcc',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skincancer',
            name='bkl',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skincancer',
            name='df',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skincancer',
            name='mel',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skincancer',
            name='nv',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='skincancer',
            name='vasc',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
