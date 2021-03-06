# Generated by Django 3.1.7 on 2021-04-10 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('ticker', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'stocks',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Thresholds',
            fields=[
                ('ticker', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('price', models.FloatField(blank=True, null=True)),
                ('threshold', models.FloatField(blank=True, null=True)),
                ('satisfied', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'thresholds',
                'unique_together': {('ticker', 'username')},
            },
        ),
        migrations.CreateModel(
            name='RealTime',
            fields=[
                ('sid', models.OneToOneField(db_column='sid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='stockapp.stocks')),
                ('dat', models.DateField()),
                ('tim', models.TimeField()),
                ('open_value', models.FloatField(blank=True, null=True)),
                ('low', models.FloatField(blank=True, null=True)),
                ('high', models.FloatField(blank=True, null=True)),
                ('close_value', models.FloatField(blank=True, null=True)),
                ('volume', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'real_time',
                'managed': True,
                'unique_together': {('sid', 'dat', 'tim')},
            },
        ),
        migrations.CreateModel(
            name='Historical',
            fields=[
                ('sid', models.OneToOneField(db_column='sid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='stockapp.stocks')),
                ('dat', models.DateField()),
                ('open_value', models.FloatField(blank=True, null=True)),
                ('low', models.FloatField(blank=True, null=True)),
                ('high', models.FloatField(blank=True, null=True)),
                ('close_value', models.FloatField(blank=True, null=True)),
                ('volume', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'historical',
                'managed': True,
                'unique_together': {('sid', 'dat')},
            },
        ),
    ]
