from django.contrib import admin
from .models import public,fund


class publicAdmin(admin.ModelAdmin):
	list_display=[f.name for f in public._meta.fields]

class fundAdmin(admin.ModelAdmin):
	list_display=[f.name for f in public._meta.fields]

admin.site.register(public,publicAdmin)
admin.site.register(fund,fundAdmin)
