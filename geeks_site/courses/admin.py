from django.contrib import admin
# from django.contrib.admin.site import register

from .models import Course, Subject


class CoursesAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    # readonly_fields = ('name',)
    list_filter = ("subject", )
    list_display = ('name', 'subject', "price", "start_date", "end_date")


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Course, CoursesAdmin)
admin.site.register(Subject, SubjectAdmin)