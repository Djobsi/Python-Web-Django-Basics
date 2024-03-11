# Generated by Django 5.0.1 on 2024-02-12 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('photos', '0003_petphoto_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='to_photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='photos.petphoto'),
        ),
    ]