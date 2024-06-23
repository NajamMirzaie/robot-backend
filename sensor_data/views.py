from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SensorData
from .serializers import SensorDataSerializer
from rest_framework import status
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

@api_view(['POST'])
def sensor_data(request):
    if request.method == 'POST':
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Return the saved data as a JSON response
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_data(request):
    if request.method == 'GET':
        # Retrieve the last 5 sensor data records
        last_five_data = SensorData.objects.all().order_by('-id')[:5]
        serializer = SensorDataSerializer(last_five_data, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_one_data(request):
    if request.method == 'GET':
        # Retrieve the last 5 sensor data records
        last_one_data = SensorData.objects.all().order_by('-id')[:1]
        serializer = SensorDataSerializer(last_one_data, many=True)
        return Response(serializer.data)


@login_required
def dashboard(request):
    context = {
        'datas': SensorData.objects.all().order_by('-id'),
        }
    return render(request, 'custom_admin_dashboard.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Username or password.')
    return render(request, 'custom_admin_login.html')