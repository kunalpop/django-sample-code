from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import City
from .serializers import CitySerializer

# Create your views here.


class ListCitiesView(APIView):
    #List all cities
    def get(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)
    

    
class CrudView(APIView):
    def get_city(self, unloc_code):
        return get_object_or_404(City, unloc_code=unloc_code)

    #Create City
    def post(self, request,unloc_code):
        city = City.objects.filter(unloc_code=unloc_code)

        if(city):
            return Response({"msg": "City already exists."},status=status.HTTP_400_BAD_REQUEST)

        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Read City
    def get(self, request, unloc_code):
        city = self.get_city(unloc_code)
        serializer = CitySerializer(city)
        return Response(serializer.data)

    #Update City
    def patch(self, request, unloc_code):
        city = self.get_city(unloc_code)
        serializer = CitySerializer(city, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Delete City
    def delete(self, request, unloc_code):
        city = self.get_city(unloc_code)
        city.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)