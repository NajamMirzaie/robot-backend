from django.db import models

class SensorData(models.Model):
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    ph = models.FloatField()
    temperature = models.FloatField()
    moisture = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'SensorData {self.id} - {self.timestamp}'
