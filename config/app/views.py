from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Car, Brand
from rest_framework import status
from .serializers import CarSerializer
from django.db import transaction
from django.core.exceptions import ValidationError


class CarAPIView(APIView):
    def get(self, request: Request, pk: int=None):
        if not pk:
            cars = Car.objects.all()
            serializer = CarSerializer(cars, many=True)
            return Response(serializer.data)
        else:
            try:
                car = Car.objects.get(pk=pk)
                serializer = CarSerializer(car)
                return Response(serializer.data)
            except Exception as e:
                return Response({"message": "Car Not Found !!!"}, status=status.HTTP_404_NOT_FOUND)
            
    def post(self, request: Request):
        serializer = CarSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            car = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)