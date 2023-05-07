from django.db import models
# https://platzi.com/clases/2694-django/45267-creando-los-modelos-question-y-choice/

# Lista de diferentes tipos de parametros:
# max_length: Especifica la longitud máxima del campo de texto (solo para campos de texto como CharField).
# default: Establece el valor predeterminado del campo. (ejemplo default=0)
# null: Permite que el campo sea nulo en la base de datos.
# blank: Permite que el campo se deje en blanco en los formularios.
# choices: Define las opciones disponibles para el campo de elección.
# upload_to: Especifica la carpeta de destino para cargar archivos (solo para campos de archivo o imagen).
# on_delete: Especifica el comportamiento de eliminación en campos de relación (por ejemplo, ondelete=models.CASCADE para eliminar en cascada).
# auto_now: Actualiza automáticamente el campo con la fecha y hora actuales cada vez que se guarda el objeto.
# auto_now_add: Establece automáticamente el campo con la fecha y hora actuales cuando se crea el objeto por primera vez.
# max_digits: Define el número máximo de dígitos permitidos en un campo decimal.
# decimal_places: Define el número de lugares decimales permitidos en un campo decimal.
# unique: Indica que el valor del campo debe ser único.
# primary_key: Establece el campo como clave primaria del modelo.
# verbose_name: Especifica el nombre legible para humanos del campo.
# https://docs.djangoproject.com/en/3.2/ref/models/fields/

# ACA SE CREAN TODOS LOS MODELOS
class MiModelo(models.Model):
    # el campo id no es necesario
    texto = models.CharField(max_length=100)  # Campo de texto de longitud limitada
    descripcion = models.TextField()  # Campo de texto de longitud variable
    edad = models.IntegerField()  # Campo para almacenar números enteros
    precio = models.FloatField()  # Campo para almacenar números de punto flotante
    fecha = models.DateField()  # Campo para almacenar fechas
    hora = models.TimeField()  # Campo para almacenar horas
    es_activo = models.BooleanField(default=False)  # Campo booleano con valor predeterminado
    # imagen = models.ImageField(upload_to='imagenes/')  # Campo para subir imágenes
    archivo = models.FileField(upload_to='archivos/')  # Campo para subir archivos
    # opcion = models.ChoiceField(choices=[('opcion1', 'Opción 1'), ('opcion2', 'Opción 2')])  # Campo de elección con opciones predefinidas
    # relacion = models.ForeignKey(OtroModelo, on_delete=models.CASCADE)  # Relación de clave externa con eliminación en cascada
    # muchos_a_muchos = models.ManyToManyField(OtroModelo)  # Relación de muchos a muchos
    objeto_json = models.JSONField()  # Campo para almacenar datos JSON
    email = models.EmailField()  # Campo para almacenar direcciones de correo electrónico
    url = models.URLField()  # Campo para almacenar URLs
    slug = models.SlugField()  # Campo para almacenar slugs
    positive_integer = models.PositiveIntegerField()  # Campo para almacenar enteros positivos
    positive_small_integer = models.PositiveSmallIntegerField()  # Campo para almacenar enteros pequeños positivos
    big_integer = models.BigIntegerField()  # Campo para almacenar enteros grandes
    decimal = models.DecimalField(max_digits=5, decimal_places=2)  # Campo para almacenar números decimales
    duration = models.DurationField()  # Campo para almacenar duraciones
    binary = models.BinaryField()  # Campo para almacenar datos binarios
    ip = models.GenericIPAddressField()  # Campo para almacenar direcciones IP
    auto_now = models.DateTimeField(auto_now=True)  # Campo de fecha y hora que se actualiza automáticamente al guardar
    auto_now_add = models.DateTimeField(auto_now_add=True)  # Campo de fecha y hora que se establece automáticamente al crear
    # encrypted = models.EncryptedTextField()  # Campo de texto encriptado
    # encrypted_char = models.EncryptedCharField(max_length=100)  # Campo de texto encriptado de longitud limitada
    # color = models.ColorField()  # Campo para almacenar valores de color
    uuid = models.UUIDField()  # Campo para almacenar identificadores únicos universales (UUID)
    small_text = models.TextField(max_length=50)  # Campo de texto de longitud limitada

# los modelos siempre tienen que ir en singular
class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)
    
    #cada vez que inovquemos el modelo en algun lado, lo que queremos es que traiga estsos atributos
    def __str__(self):
        return self.name
    
    def metodo_personalizado(self):
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