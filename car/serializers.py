from rest_framework import serializers
from car.models import Car
from django.core.validators import MinValueValidator, MaxValueValidator


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1914)]
    )
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(
        allow_null=True, required=False, allow_blank=True
    )

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "manufacturer": instance.manufacturer,
            "model": instance.model,
            "horse_powers": instance.horse_powers,
            "is_broken": instance.is_broken,
            "problem_description": instance.problem_description,
        }
