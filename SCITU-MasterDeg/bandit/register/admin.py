from django.contrib import admin
from .models import reg


class regAdmin(admin.ModelAdmin):
	list_display=[f.name for f in reg._meta.fields]

admin.site.register(reg,regAdmin)
