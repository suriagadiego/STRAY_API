from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from django.shortcuts import get_object_or_404
from ..serializers import CompanyFeedingCountSerializer, TransactionSerialzier
from ..models import Company, ActivityType, Counter, CompanyFeedingCount
from django.db.models import F


def compose_transaction(company_id, body):
    transaction_data = {
        "company_id": company_id,
        "activity_type": ActivityType.FEED,
        "strays_affected": body["count"],
        "price": body["count"]*25
    }
    return transaction_data


def update_total_strays_fed(increment_value):
    target_uuid = '4b8f464f-1a67-46dd-b843-970609ddada7'
    counters = Counter.objects.filter(uuid=target_uuid)
    counters.update(total_count=F('total_count') + increment_value)

def update_or_create_company_feeding_count(company_id, increment_value):
    company_feeding_count = CompanyFeedingCount.objects.filter(company_id=company_id).first()
    if company_feeding_count:
        company_counter = CompanyFeedingCount.objects.filter(company_id=company_id)
        company_counter.update(total_count=F('total_count') + increment_value)
    
    else:
        data = {
            "company_id": company_id,
            "total_count": increment_value
        }

        company_feeding_count_serializer = CompanyFeedingCountSerializer(data=data)
        if company_feeding_count_serializer.is_valid():
            company_feeding_count_serializer.save()

        else:
            return Response(company_feeding_count_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def feed_stray(request, company_uuid):
    company = get_object_or_404(Company, uuid=company_uuid)
    company_id = company.company_id

    transaction_dict = compose_transaction(company_id, request.data)
    serializer = TransactionSerialzier(data=transaction_dict)
    increment_value = request.data['count']

    if serializer.is_valid():
        serializer.save()
        company_feed_count_errors = update_or_create_company_feeding_count(company_id, increment_value)
        update_total_strays_fed(increment_value)
        if company_feed_count_errors:
            return Response(company_feed_count_errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# TODO: Fix all return response
# list all future upgrades
# list all potential problems
# Update Reamde