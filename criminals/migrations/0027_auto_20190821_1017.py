# Generated by Django 2.2.2 on 2019-08-21 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0026_auto_20190819_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='permit',
            field=models.CharField(max_length=11),
        ),
    ]
