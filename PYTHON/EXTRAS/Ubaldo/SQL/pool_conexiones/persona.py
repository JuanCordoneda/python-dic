from logger_base import logger

class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, apodo=None):
        self.__id_persona = id_persona
        self.__nombre = nombre
        self.__apellido = apellido
        self.__apodo = apodo

    def __str__(self):
        return (
            f'Id Persona: {self.__id_persona}, '
            f'Nombre: {self.__nombre}, '
            f'Apellido: {self.__apellido}, '
            f'apodo: {self.__apodo}'
        )

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_apodo(self):
        return self.__apodo

    def set_apodo(self, apodo):
        self.__apodo = apodo

    def get_id_persona(self):
        return self.__id_persona

    def set_id_persona(self, id_persona):
        self.__id_persona = id_persona


if __name__ == '__main__':
    persona1 = Persona(1, 'Juan', 'Perez', 'apodo')
    logger.debug(persona1)
    # simulando un objeto a insertar de tipo persona
    persona2 = Persona(nombre='Karla', apellido='Gomez',
                       apodo='kgomez@mail.com')
    logger.debug(persona2)
    # simular el caso de eliminar un objeto de tipo persona
    persona3 = Persona(id_persona=3)
    logger.debug(persona3)
