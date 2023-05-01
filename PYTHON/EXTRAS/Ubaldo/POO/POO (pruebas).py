class Operaciones:
  def __init__(self,op1,op2):
    self.op1= op1
    self.op2= op2

  def restar(self):
    return self.op1 - self.op2
  def sumar(self):
    return self.op1 + self.op2
  def multiplicar(self):
    return self.op1 * self.op2
  def dividir(self):
    return self.op1 / self.op2


operaciones = Operaciones(8,2)
print(operaciones.restar())
print(operaciones.sumar())
print(operaciones.multiplicar())
print(operaciones.dividir())

.........................................................................................................
class Lista:
    def __init__(self,p1,e,r):
        self.__p1=p1                 #encapsulamiento
        self.__e=e        
        self.__r=r

    def invitar(self):
        return 'invité a',self.__p1,'que tiene',self.__e,'años y me llevo',self.__r
    
    def self_p1(self,p1):    #funcion para cambiar variables
        self.__p1 = p1
    def self_e(self,e):
        self.__e = e
    def self_r(self,r):
        self.__r = r

borgo = Lista('sorgo',20,'bien')
borgo.self_e(21)             #cambiando edad
borgo.self_r('perfecto')     #cambiando relacion
print(borgo.invitar())
tito = Lista('tito',20,'muy bien')
print(tito.invitar())
juani = Lista('juani',20,'muy bien')
print(juani.invitar())

.........................................................................................................

class Rectangulo:
  def __init__(self,base,altura):
    self.base=base
    self.altura=altura
  def area(self):
    return 'el area del rectangulo es:',self.base*self.altura

rectangulo=Rectangulo(6,9)
print(rectangulo.area())

.........................................................................................................

class Caja:
  def __init__(self,ancho,largo,alto):
    self.ancho=ancho
    self.largo=largo
    self.alto=alto
  def volumen(self):
    return 'el volumen es:',self.ancho*self.alto*self.largo
  
ancho=int(input('dime el ancho:' )) 
largo=int(input('dime el largo: '))  
alto=int(input('dime el alto: ')) 

caja1= Caja(ancho,largo,alto)
print(caja1.volumen())

.........................................................................................................
