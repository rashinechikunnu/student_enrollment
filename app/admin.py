from django.contrib import admin
from .models import student_data,Class_room,Subject,Enrollment

# Register your models here.

admin.site.register(student_data),
admin.site.register(Class_room),
admin.site.register(Subject),
admin.site.register(Enrollment),



