from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import City
from .serializers import CitySerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

json_schema = openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "unloc_code": openapi.Schema(type=openapi.TYPE_STRING),
                "name": openapi.Schema(type=openapi.TYPE_STRING),
                "city": openapi.Schema(type=openapi.TYPE_STRING),
                "country": openapi.Schema(type=openapi.TYPE_STRING),
                "province": openapi.Schema(type=openapi.TYPE_STRING),
                "timezone": openapi.Schema(type=openapi.TYPE_STRING),
                "alias": openapi.Schema(type=openapi.TYPE_ARRAY,items=openapi.Items(type=openapi.TYPE_STRING)),
                "region": openapi.Schema(type=openapi.TYPE_ARRAY,items=openapi.Items(type=openapi.TYPE_STRING)),
                "coordinates_lat": openapi.Schema(type=openapi.TYPE_NUMBER),
                "coordinates_lon": openapi.Schema(type=openapi.TYPE_NUMBER),
                "code": openapi.Schema(type=openapi.TYPE_STRING),
            },
            example={
                    "unloc_code": "NWCTY",
                    "name": "NEWCITY",
                    "city": "New City",
                    "country": "Zimbabwe",
                    "province": "Manicaland",
                    "timezone": "Africa/Harare",
                    "alias": [],
                    "regions": [],
                    "coordinates_lat": -19.9757714,
                    "coordinates_lon": 31.650351,
                    "code": "55555"
            }
        )

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
    @swagger_auto_schema(request_body=json_schema,responses={200: json_schema}) 
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
    @swagger_auto_schema(request_body=json_schema,responses={200: json_schema})
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