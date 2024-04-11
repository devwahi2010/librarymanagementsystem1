from django.urls import path
from . import views

urlpatterns = [
    # Publisher URLs
    path('publishers/', views.publisher_list, name='publisher_list'),
    path('publishers/<int:pk>/', views.publisher_detail, name='publisher_detail'),
    path('publishers/create/', views.publisher_create, name='publisher_create'),
    path('publishers/<int:pk>/update/', views.publisher_update, name='publisher_update'),
    path('publishers/<int:pk>/delete/', views.publisher_delete, name='publisher_delete'),

    # Book URLs
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/create/', views.book_create, name='book_create'),
    path('books/<int:pk>/update/', views.book_update, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),

    # Reader URLs
    path('readers/', views.reader_list, name='reader_list'),
    path('readers/<int:pk>/', views.reader_detail, name='reader_detail'),
    path('readers/create/', views.reader_create, name='reader_create'),
    path('readers/<int:pk>/update/', views.reader_update, name='reader_update'),
    path('readers/<int:pk>/delete/', views.reader_delete, name='reader_delete'),

    # Reservation URLs
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservations/<int:pk>/', views.reservation_detail, name='reservation_detail'),
    path('reservations/create/', views.reservation_create, name='reservation_create'),
    path('reservations/<int:pk>/update/', views.reservation_update, name='reservation_update'),
    path('reservations/<int:pk>/delete/', views.reservation_delete, name='reservation_delete'),

    # Staff URLs
    path('staff/', views.staff_list, name='staff_list'),
    path('staff/<int:pk>/', views.staff_detail, name='staff_detail'),
    path('staff/create/', views.staff_create, name='staff_create'),
    path('staff/<int:pk>/update/', views.staff_update, name='staff_update'),
    path('staff/<int:pk>/delete/', views.staff_delete, name='staff_delete'),

    # Report URLs
    path('reports/', views.report_list, name='report_list'),
    path('reports/<int:pk>/', views.report_detail, name='report_detail'),
    path('reports/create/', views.report_create, name='report_create'),
    path('reports/<int:pk>/update/', views.report_update, name='report_update'),
    path('reports/<int:pk>/delete/', views.report_delete, name='report_delete'),

    path('', views.home_page, name='home'),
    path('dashboard/', views.dashboard_page, name='dashboard'),
]
