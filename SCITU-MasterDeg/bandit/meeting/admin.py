from django.contrib import admin
from .models import meetingTable,report


class meetingTableAdmin(admin.ModelAdmin):
	list_display=[f.name for f in meetingTable._meta.fields]

class reportsAdmin(admin.ModelAdmin):
	list_display=[f.name for f in report._meta.fields]


admin.site.register(meetingTable,meetingTableAdmin)
admin.site.register(report,reportsAdmin)
