from django.contrib import admin
from .models import Task,Profile
from .models import Project


admin.site.register(Task)
admin.site.register(Profile)
admin.site.register(Project)
