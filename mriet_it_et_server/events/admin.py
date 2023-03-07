from django.contrib import admin

from events.models import Payment, Student, Stu_Coordinator

# Register your models here.
admin.site.register(Student)
admin.site.register(Payment)
admin.site.register(Stu_Coordinator)