# Generated by Django 2.2.2 on 2019-08-19 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('criminals', '0025_auto_20190808_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrafficOffence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traffic_offence', models.CharField(max_length=100)),
                ('enactment', models.CharField(max_length=200)),
                ('fixed_penalty', models.CharField(max_length=10)),
                ('penalty_points', models.CharField(max_length=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='time_of_offence',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date_time_of_offence',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='offence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criminals.TrafficOffence'),
        ),
    ]