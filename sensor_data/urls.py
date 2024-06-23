from django.urls import path
from . import views

urlpatterns = [
    path('sensor-data/', views.sensor_data, name='save_sensor_data'),
    path('get-data/', views.get_data, name='get_data'),
    path('get-one-data/', views.get_one_data, name='get_one_data'),

]
