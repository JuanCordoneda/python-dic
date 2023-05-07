# EL ADMIN ES UN LUGAR QUE TE PERMITE VER TODOS LOS DATOS COMO ADMINISTRADOR
# http://127.0.0.1:8000/admin
from django.contrib import admin
from .models import Employee,Role,Department

# Register your models here.
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)