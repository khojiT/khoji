from django.contrib import admin
from .models import Project , First

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['subject']

admin.site.register(Project,ProjectAdmin)
admin.site.register(First)
