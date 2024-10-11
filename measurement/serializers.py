from rest_framework import serializers

from measurement.models import Sensor, Measurement


# TODO: опишите необходимые сериализаторы
class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = serializers.SerializerMethodField()

    def get_measurements(self, obj):
        return [
            {
                "temperature": measurement.temperature,
                "created_at": measurement.created_at.isoformat(),
            }
            for measurement in obj.measurement_set.all()
        ]

    class Meta:
        model = Sensor
        fields = ["id", "name", "description", "measurements"]