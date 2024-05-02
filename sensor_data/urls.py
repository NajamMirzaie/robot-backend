from django.urls import path
from . import views

urlpatterns = [
    path('sensor-data/', views.sensor_data, name='save_sensor_data'),
]
