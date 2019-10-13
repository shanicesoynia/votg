# Generated by Django 2.2.2 on 2019-08-22 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0030_remove_report_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='alias',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='notes',
            field=models.CharField(default='', max_length=2000),
        ),
    ]