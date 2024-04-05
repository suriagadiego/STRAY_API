from rest_framework import serializers
from .models import Transaction, Company, Counter, CompanyFeedingCount

class TransactionSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class CompanySerialzier(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = '__all__'


class CompanyFeedingCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyFeedingCount
        fields = '__all__'
