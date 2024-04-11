# library/views.py
from django.shortcuts import render
from .models import Publisher, Book, Reader, DateOfReserveReturn, Staff, Report

# Implement views for CRUD operations
# library/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Publisher, Book, Reader, DateOfReserveReturn, Staff, Report
from .forms import PublisherForm, BookForm, ReaderForm, ReservationForm, StaffForm, ReportForm

# Publisher views
def publisher_list(request):
    publishers = Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publishers': publishers})

def publisher_detail(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    return render(request, 'publisher_detail.html', {'publisher': publisher})

def publisher_create(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')
    else:
        form = PublisherForm()
    return render(request, 'publisher_form.html', {'form': form})
def publisher_detail(request, publisher_id):
    publisher = get_object_or_404(Publisher, pk=publisher_id)
    context = {'publisher': publisher}
    return render(request, 'publisher_detail.html', context)



def publisher_update(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)

    if request.method == 'POST':
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')  # Redirect to the correct URL
    else:
        form = PublisherForm(instance=publisher)

    return render(request, 'publisher_form.html', {'form': form, 'publisher': publisher})
def publisher_delete(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'POST':
        publisher.delete()
        return redirect('publisher_list')
    return render(request, 'publisher_confirm_delete.html', {'publisher': publisher})

# Book views
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})




def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to the book list upon successful update
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form, 'book': book})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})

# Reader views
def reader_list(request):
    readers = Reader.objects.all()
    return render(request, 'reader_list.html', {'readers': readers})

def reader_detail(request, pk):
    reader = get_object_or_404(Reader, pk=pk)
    return render(request, 'reader_detail.html', {'reader': reader})

def reader_create(request):
    if request.method == 'POST':
        form = ReaderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reader_list')
    else:
        form = ReaderForm()
    return render(request, 'reader_form.html', {'form': form})





def reader_update(request, pk):
    reader = get_object_or_404(Reader, pk=pk)
    if request.method == 'POST':
        form = ReaderForm(request.POST, instance=reader)
        if form.is_valid():
            form.save()
            return redirect('reader_list')  # Assuming 'reader_list' is the name of your reader list view
    else:
        form = ReaderForm(instance=reader)
    return render(request, 'reader_form.html', {'form': form})


def reader_delete(request, pk):
    reader = get_object_or_404(Reader, pk=pk)
    if request.method == 'POST':
        reader.delete()
        return redirect('reader_list')
    return render(request, 'reader_confirm_delete.html', {'reader': reader})

# DateOfReserveReturn views
def reservation_list(request):
    reservations = DateOfReserveReturn.objects.all()
    return render(request, 'reservation_list.html', {'reservations': reservations})

def reservation_detail(request, pk):
    reservation = get_object_or_404(DateOfReserveReturn, pk=pk)
    return render(request, 'reservation_detail.html', {'reservation': reservation})

def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'reservation_form.html', {'form': form})

def reservation_update(request, pk):
    reservation = get_object_or_404(DateOfReserveReturn, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservation_form.html', {'form': form})

def reservation_delete(request, pk):
    reservation = get_object_or_404(DateOfReserveReturn, pk=pk)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')
    return render(request, 'reservation_confirm_delete.html', {'reservation': reservation})

# Staff views
def staff_list(request):
    staff = Staff.objects.all()
    return render(request, 'staff_list.html', {'staff': staff})

def staff_detail(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    return render(request, 'staff_detail.html', {'staff': staff})

def staff_create(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm()
    return render(request, 'staff_form.html', {'form': form})

def staff_update(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
            return redirect('staff_list')
    else:
        form = StaffForm(instance=staff)
    return render(request, 'staff_form.html', {'form': form})

def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.delete()
        return redirect('staff_list')
    return render(request, 'staff_confirm_delete.html', {'staff': staff})

# Report views
def report_list(request):
    reports = Report.objects.all()
    return render(request, 'report_list.html', {'reports': reports})

def report_detail(request, pk):
    report = get_object_or_404(Report, pk=pk)
    return render(request, 'report_detail.html', {'report': report})

def report_create(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = ReportForm()
    return render(request, 'report_form.html', {'form': form})

def report_update(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('report_list')
    else:
        form = ReportForm(instance=report)
    return render(request, 'report_form.html', {'form': form})

def report_delete(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        report.delete()
        return redirect('report_list')
    return render(request, 'report_confirm_delete.html', {'report': report})

def home_page(request):
    return render(request, 'home.html')



def dashboard_page(request):
    return render(request, 'dashboard.html')



from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.middleware.csrf import get_token

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def home_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'root' and password == 'system':
            # Authenticate the user with the provided username and password
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # If authentication is successful, log in the user
                login(request, user)
                # Redirect the user to the dashboard page
                return redirect('dashboard')
    # If the request method is not POST or authentication fails, render the home page
    return render(request, 'home.html')
