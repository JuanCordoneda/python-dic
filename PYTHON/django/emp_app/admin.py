# EL ADMIN ES UN LUGAR QUE TE PERMITE VER TODOS LOS DATOS COMO ADMINISTRADOR
# http://127.0.0.1:8000/admin
# https://platzi.com/clases/2728-django-intermedio/45825-mejorando-el-admin-change-list/
# https://docs.djangoproject.com/en/4.0/ref/contrib/admin/
from django.contrib import admin
from .models import Employee,Role,Department

# Register your models here.
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin): 
    #ordena los campos de la tabla admin segun el orden que queramos
    fields = ["pub_date", "question_text"] 
    # Agrega campos a la tabla
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # Que filtrar en la vista de Questions (se agrega una lista de filtros)
    list_filter = ['pub_date']
    # Tipo de busqueda (se agrega un buscador)
    search_fields=['question_text']
    #Agrupar los fields en sectores
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        #Date information se agrega un collapse
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    #Agregando la clase creada
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)