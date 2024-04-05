from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from ..serializers import CompanySerialzier

@api_view(['POST'])
def sign_up(request):
    serializer = CompanySerialzier(data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    response = {
        "company_name": serializer.data["company_name"],
        "UUID": serializer.data["uuid"]
    }

    return Response(response, status=status.HTTP_201_CREATED)   