from django.contrib import admin
from .models import SensorData

class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'nitrogen', 'phosphorus', 'potassium', 'ph', 'temperature', 'moisture', 'timestamp')
    search_fields = ('id', 'timestamp')
    list_filter = ('timestamp',)

admin.site.register(SensorData, SensorDataAdmin)
