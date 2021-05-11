from django.db import models
from django.contrib.auth.models import User


class Historical(models.Model):
    sid = models.OneToOneField('Stocks', models.DO_NOTHING, db_column='sid', primary_key=True)
    dat = models.DateField()
    open_value = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    close_value = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'historical'
        unique_together = (('sid', 'dat'),)


class RealTime(models.Model):
    sid = models.OneToOneField('Stocks', models.DO_NOTHING, db_column='sid', primary_key=True)
    dat = models.DateField()
    tim = models.TimeField()
    open_value = models.FloatField(blank=True, null=True)
    low = models.FloatField(blank=True, null=True)
    high = models.FloatField(blank=True, null=True)
    close_value = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'real_time'
        unique_together = (('sid', 'dat', 'tim'),)


class Stocks(models.Model):
    sid = models.IntegerField(primary_key=True)
    ticker = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'stocks'

    def __str__(self):
    	return self.ticker

