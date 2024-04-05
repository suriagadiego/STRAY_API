from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from django.shortcuts import get_object_or_404
from ..models import Counter, CompanyFeedingCount, Company



@api_view(['GET'])
def get_total_fed(request):
    target_uuid = '4b8f464f-1a67-46dd-b843-970609ddada7'
    counter = Counter.objects.get(uuid=target_uuid)

    return Response({'total_strays_fed': counter.total_count}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_total_fed_by_company(request, company_uuid):
    company = get_object_or_404(Company, uuid=company_uuid)
    company_id = company.company_id
    company_name = company.company_name

    company_feeding_count = get_object_or_404(CompanyFeedingCount, company_id = company_id)

    response = {
        "total_strays_fed": company_feeding_count.total_count,
        "company_name": company_name
    }

    return Response(response, status=status.HTTP_200_OK)