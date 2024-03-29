# Generated by Django 5.0.1 on 2024-02-06 11:45

import django.core.validators
import forms_advanced.web.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.PositiveSmallIntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=32, validators=[forms_advanced.web.models.validate_first_name, django.core.validators.MinLengthValidator(2)]),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=32, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
