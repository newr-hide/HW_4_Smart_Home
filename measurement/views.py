from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer

# Показать усе датчики

class SensorViews(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Датчики переименовать описание
class SensorsViews(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    lookup_field = 'pk'

    def get(self, request, pk):
        queryset = Sensor.objects.all()
        sensor = self.get_queryset().get(id=pk)
        serializer = SensorDetailSerializer(sensor)
        return Response(serializer.data)

    def get_object(self):

        return self.get_queryset().get(id=self.kwargs['pk'])

    def put(self, request, *args, **kwargs):
        sensor = self.get_object()
        serializer = self.serializer_class(sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        sensor = self.get_object()
        serializer = self.serializer_class(sensor, data=request.data, partial=True)
        if serializer.is_valid():
            sensor = serializer.save()
            return Response({"detail": "Объект успешно изменён."})

# Температуру занести
class MeasurementViews(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










