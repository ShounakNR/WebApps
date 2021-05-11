from rest_framework import serializers

from django.contrib.auth.models import User
from stockapp.models import Historical, RealTime, Stocks

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_staff')


# Serializers define the API representation.
class HistoricalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Historical
        fields = ('sid', 'dat', 'open_value', 'low', 'high', 'close_value', 'volume')


# Serializers define the API representation.
class RealTimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RealTime
        fields = ('sid', 'dat', 'tim', 'open_value', 'low', 'high', 'close_value', 'volume')


# Serializers define the API representation.
class TickerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stocks
        fields = ('sid', 'ticker')

