from django.db import models
from django.contrib import admin
class BOOK(models.Model):
    BOOK_TITLE=models.CharField(max_length=50,primary_key=True);
    BOOK_PAGES=models.IntegerField();
    BOOK_AUTHOR=models.CharField(max_length=50);
    BOOK_PRICE=models.DecimalField(max_digits=10,decimal_places=True);
    BOOK_CHAPTER=models.CharField(max_length=50);
class BOOKAdmin(admin.ModelAdmin):
    list_display=("BOOK_TITLE","BOOK_PAGES","BOOK_AUTHOR","BOOK_PRICE","BOOK_CHAPTER");