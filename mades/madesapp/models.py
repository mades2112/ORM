from django.db import models
from django.contrib import admin
class Bus(models.Model):
     Bus_id=models.CharField( max_length=20,primary_key=True);
     Bus_name=models.CharField(max_length=20);
     start_time=models.TimeField();
     end_time=models.TimeField();
     start_station_code=models.CharField(max_length=20);
class BusAdmin(admin.ModelAdmin):
     list_display=("Bus_id","Bus_name","start_time","end_time","start_station_code");