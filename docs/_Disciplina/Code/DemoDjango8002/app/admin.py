from django.contrib import admin
from app.models import Aluno, Employee, Department

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'department')
    search_fields = ('name','role',)
    list_filter = ('department',) #filter
    ordering = ('name',)
    
admin.site.register(Aluno)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department)