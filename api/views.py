from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import ProfileSerializer, CustomersSerializer
from accounts.models import Profile
from customers.models import Customers

@api_view(['GET'])
def getinstructors(request):
    instructors = Profile.objects.all()
    serializer = ProfileSerializer(instructors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getinstructor(request, id):
    instructor = Profile.objects.get(id=id)
    serializer = ProfileSerializer(instructor, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getcustomers(request):
    instructors = Customers.objects.all()
    serializer = CustomersSerializer(instructors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getcustomer(request, id):
    customers = Customers.objects.get(id=id)
    serializer = CustomersSerializer(customers, many=False)
    return Response(serializer.data)
