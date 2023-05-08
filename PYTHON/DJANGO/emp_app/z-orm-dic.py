from emp_app.models import Employee,Role 
from django.shortcuts import get_object_or_404
# -------------------------------------GET---------------------------------------------------------
Employee.objects.all()                 #GET ALL AL MODELO
Role.objects.get(name='Juan Cruz')     #GET AL MODELO (1 SOLO OBJETO)
Role.objects.filter(name='Juan Cruz')  #GET AL MODELO (+ DE 1 OBJETO)
#QUERIES CON __ https://docs.djangoproject.com/en/3.2/topics/db/queries/#field-lookups-intro
# -------------------------------------FILTER---------------------------------------------------------
Role.objects.filter(name_text__startswith='Juan Cruz')  #EMPIEZA CON...
# __gt = Mayor que
# __gte = Mayor o igual que
# __lt = Menor que
# __lte = Menos o igual que
# __startswith = Empieza con
# __endswith = Termina con    
emps_filter = get_object_or_404(Employee, name='Juan Cruz') #FILTRA Y SI NO ESTA, 404
# -------------------------------------ORDER BY---------------------------------------------------------
Role.objects.order_by('-name')[:5]  #SOLO LOS 5 ELEM
# -------------------------------------INSERT---------------------------------------------------------
registro=Role(name='Juan Cruz') #INSERT AL MODELO parte 1
registro.save() #parte 2
registro.name #juan cruz
# -------------------------------------CLAVES FORANEAS---------------------------------------------------------
registro.name_set.all() #trae todos los registros asociados al nombre
registro.name_set.count(campos) #cuenta registros asociados al nombre
registro.name_set.create(campos) #crea registros asociados al nombre
# -------------------------------------RECORRER REGISTROS---------------------------------------------------------
for elem in registro.name_set.all():
    # print elem.name

# https://platzi.com/clases/2694-django/45272-accediendo-al-conjunto-de-respuestas/
# https://docs.djangoproject.com/en/3.2/topics/db/queries/#field-lookups-intro