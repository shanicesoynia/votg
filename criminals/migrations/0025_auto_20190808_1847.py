# Generated by Django 2.2.2 on 2019-08-08 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0024_auto_20190806_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.FileField(upload_to=''),
        ),
    ]
