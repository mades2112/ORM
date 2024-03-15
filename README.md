# Ex02 Django ORM Web Application
## Date:27/03/24

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![alt text](<Screenshot 2024-03-15 052715.png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py
from django.contrib import admin
from .models import Bus,BusAdmin
admin.site.register(Bus,BusAdmin)
```
```
models.py
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
```
## OUTPUT
![Screenshot 2024-03-15 171409](https://github.com/mades2112/ORM/assets/152461996/d304f507-cc6d-47bb-941d-4f42083540e6)



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
