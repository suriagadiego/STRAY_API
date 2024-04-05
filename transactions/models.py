from django.db import models
import uuid

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    company_name = models.CharField(max_length=80, null=False, unique=True)
    description = models.TextField(null=True, blank=True)


class ActivityType(models.TextChoices):  # Django TextChoices for enums
    FEED = 'FEED'
    SPAY = 'SPAY'


class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50, choices=ActivityType.choices)
    strays_affected = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)


class Counter(models.Model):
    counter_id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    activity_type = models.CharField(max_length=50, choices=ActivityType.choices)
    total_count = models.IntegerField()


class CompanyFeedingCount(models.Model):
    feed_count_id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    total_count = models.IntegerField()
