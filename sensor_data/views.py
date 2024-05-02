from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SensorData
from .serializers import SensorDataSerializer

@api_view(['GET', 'POST'])
def sensor_data(request):
    if request.method == 'GET':
        # Query the database for the last 5 records of sensor data
        last_five_data = SensorData.objects.order_by('-timestamp')[:5]
        
        # Serialize the data
        serializer = SensorDataSerializer(last_five_data, many=True)
        
        # Return the serialized data as a JSON response
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Return the saved data as a JSON response
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
