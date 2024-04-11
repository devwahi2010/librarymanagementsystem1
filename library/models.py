# library/models.py
from django.db import models

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

class Reader(models.Model):
    reader_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class DateOfReserveReturn(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reserve_date = models.DateField()
    return_date = models.DateField()

class Staff(models.Model):
    staff_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

class Report(models.Model):
    report_text = models.TextField()
    report_date = models.DateField()
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
