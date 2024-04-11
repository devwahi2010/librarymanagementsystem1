# library/forms.py
from django import forms
from .models import Publisher, Book, Reader, DateOfReserveReturn, Staff, Report

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['publisher_name', 'location']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher']

class ReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['reader_name', 'email']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = DateOfReserveReturn
        fields = ['reader', 'book', 'reserve_date', 'return_date']

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['staff_name', 'position']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['report_text', 'report_date']
