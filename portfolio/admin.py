from django.contrib import admin
from .models import Project


# Register your models here.          registrod de los modelos en el administrador 

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
   


admin.site.register(Project, ProjectAdmin)    






