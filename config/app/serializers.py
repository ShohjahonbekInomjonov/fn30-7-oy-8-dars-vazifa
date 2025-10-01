from rest_framework import serializers
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Car, Brand

class BrandSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Brand.objects.create(**validated_data)


class CarSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    year = serializers.IntegerField(validators=[MinValueValidator(1885), MaxValueValidator(2025)])
    color = serializers.CharField(max_length=255)
    brand_id = serializers.IntegerField()

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    class Meta:
        model = Car
        fields = '__all__'
