
from django.contrib import admin
from .models import  Publisher,Book,Reader,DateOfReserveReturn,Staff

admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(DateOfReserveReturn)
admin.site.register(Staff)

