from django.db import models

# Lista de diferentes tipos de models.CharField en Django:
# 1. CharField: Almacena texto corto con una longitud máxima determinada por max_length.
# 2. TextField: Almacena texto largo con una longitud potencialmente ilimitada.
# 3. SlugField: Almacena identificadores de URL legibles por humanos.
# 4. EmailField: Almacena direcciones de correo electrónico válidas.
# 5. URLField: Almacena direcciones URL válidas.
# 6. BooleanField: Almacena valores booleanos (True o False).
# 7. DateField: Almacena fechas.
# 8. DateTimeField: Almacena fechas y horas.
# 9. TimeField: Almacena horas.
# 10. IntegerField: Almacena números enteros.
# 11. PositiveIntegerField: Almacena números enteros positivos.
# 12. PositiveSmallIntegerField: Almacena números enteros positivos más pequeños que un entero normal.
# 13. SmallIntegerField: Almacena números enteros más pequeños que un entero normal.

# ACA SE CREAN TODOS LOS MODELOS
class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Role(models.Model):
    name = models.CharField(max_length=100,null=False)
    
    def __str__(self):
        return self.name
    



class Employee(models.Model):
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()
    
    def __str__(self):
        return "%s %s %s" %(self.first_name, self.last_name, self.phone)