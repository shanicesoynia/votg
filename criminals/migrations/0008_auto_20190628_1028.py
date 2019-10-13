# Generated by Django 2.2.2 on 2019-06-28 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0007_auto_20190628_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offence',
            name='person',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='enactment',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='fixed_penalty',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='offender',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='offence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criminals.Offence'),
        ),
    ]