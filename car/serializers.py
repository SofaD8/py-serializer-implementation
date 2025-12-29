from rest_framework import serializers
from car.models import Car
from django.core.validators import MaxValueValidator, MinValueValidator


class CarSerializer(serializers.Serializer):
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1914)]
    )
    is_broken = serializers.BooleanField()
    problem_description = (
        serializers.CharField(allow_null=True, required=False)
    )

    def create(self, validated_data):
        return Car(**validated_data)

    def to_representation(self, instance):
        return {
            "manufacturer": instance.manufacturer,
            "model": instance.model,
            "horse_powers": instance.horse_powers,
            "is_broken": instance.is_broken,
            "problem_description": instance.problem_description,
        }
