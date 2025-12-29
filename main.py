import json
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return json.dumps(
        serializer.data,
        separators=(",", ":")
    ).encode("utf-8")

def deserialize_car_object(data: bytes) -> Car:
    parsed = json.loads(data.decode("utf-8"))
    serializer = CarSerializer(data=parsed)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
