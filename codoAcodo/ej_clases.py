'''
1) Crear la clase Persona con los métodos “set_nombre”, “set_edad”, “get_nombre”, “get_edad” y “print_persona”. Luego crear dos objetos del tipo Persona e imprimirlos por consola.
'''
from os import name


class Persona:
    nombre = ""
    edad = ""
    #ej 2
    def __init__(self, nom, e):
        self.nombre=nom
        self.edad=e

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}. Edad: {self.edad}'
         
    def set_nombre(self, nom):
        self.nombre = nom

    def set_edad(self, e):
        self.edad = e

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def mayor_de_edad(self):
        if self.edad > 18:
            return True
        else:
            return False

    def es_mayor_que(self, persona):
        edad1=Persona.get_edad(self)
        edad2=Persona.get_edad(persona)
        if edad1 > edad2:
            return True
        else:
            return False

    @staticmethod
    def get_mayor(persona1,persona2):
        edad1=Persona.get_edad(persona1)
        edad2=Persona.get_edad(persona2)
        if edad1 == edad2:
            return "las dos personas tienen la misma edad"
        elif edad1 > edad2:
            return persona1
        else:
            return persona2


    #Método para impimir los datos, no es necesario
    # def imprimir(self):
    #     print(f'Nombre: {self.nombre}. Edad: {self.edad}')

persona1 = Persona("Alan",12)
persona2 = Persona("Elsa",65)
Persona.set_nombre(persona1, "Daniela")
Persona.set_edad(persona1, 14)
'''
persona1.imprimir()
#Diferentes formas de llamar los métodos
# Persona.inicializar(persona1,"Alan",32)
# Persona.imprimir(persona1)
# Persona.imprimir(persona1)
print(Persona.get_nombre(persona1))
print(Persona.get_edad(persona1))
print(persona1.get_nombre())
print(persona1.get_eda())
'''


'''
2) Agregarle a la clase anterior un constructor que reciba nombre y edad.
'''

'''
persona2=Persona()
persona2.inicializar("Juan", 40)
print(persona2.get_nombre(), persona2.get_edad())
'''


'''
3) Agregarle a la clase anterior un método “es_mayor_de_edad” que devuelva True o False.
'''
'''
print(persona1.mayor_de_edad())
print(persona2.mayor_de_edad())
'''

'''
4) Agregarle un método “es_mayor_que” el cual recibe un objeto persona y compara su edad con la del objeto actual.
'''
'''
print(persona2.nombre, "es mayor que", persona1.nombre, "?", persona2.es_mayor_que(persona1))
'''


'''
5) Agregarle un método estático “get_mayor” que reciba dos objetos Persona y devuelva el de edad mayor.
'''
'''
print("Persona de mayor edad:", Persona.get_mayor(persona1, persona2))
'''

'''
6) Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.´
'''
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota
    def print(self):
        print(f'Nombre: {self.nombre}')
        print(f'Nota: {self.nota}')
    def aprobado(self):
        if self.nota > 7:
            print("Está aprobado")
        else:
            print("Está desaprobado")

'''
alumno1=Alumno("Alan",8)
alumno1.print()
alumno1.aprobado()
'''
'''
7) Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno).
'''
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3
    def ladoMayor(self):
        if self.lado1>=self.lado2 and self.lado1>=self.lado3:
            print(f'El lado mayor mide {self.lado1}')
        elif self.lado2>=self.lado1 and self.lado2>=self.lado3:
            print(f'El lado mayor mide {self.lado2}')
        else:
            print(f'El lado mayor mide {self.lado3}')
    def tipoTriangulo(self):
        if self.lado1==self.lado2==self.lado3:
            print("Equilatero")
        elif self.lado1==self.lado2 or self.lado1==self.lado3 or self.lado2==self.lado3:
            print("Isósceles")
        else:
            print("Escaleno")
    #Alternativa todo junto. Es muy engorrosa, no me gustó
    def caracteristicas(self):
        if self.lado1==self.lado2==self.lado3:
            print(f'Lado mayor: {self.lado1}')
            print(f'Tipo de triangulo: Equilatero')
        elif (self.lado1==self.lado2 and self.lado1>self.lado3) \
            or (self.lado1==self.lado3 and self.lado1>self.lado2) \
            or (self.lado2==self.lado3 and self.lado1>self.lado3):
            print(f'Lado mayor: {self.lado1}')
            print(f'Tipo de triangulo: Isósceles')
        elif (self.lado1==self.lado3 and self.lado2>self.lado1) \
            or (self.lado2==self.lado3 and self.lado2>self.lado1):
            print(f'Lado mayor: {self.lado2}')
            print(f'Tipo de triangulo: Isósceles')
        elif (self.lado1==self.lado2 and self.lado3>self.lado1):
            print(f'Lado mayor: {self.lado3}')
            print(f'Tipo de triangulo: Isósceles')
        elif self.lado1>self.lado2 and self.lado1>self.lado3:
            print(f'Lado mayor: {self.lado1}')
            print(f'Tipo de triangulo: Escaleno')
        elif self.lado2>self.lado1 and self.lado2>self.lado3:
            print(f'Lado mayor: {self.lado2}')
            print(f'Tipo de triangulo: Escaleno')
        else:
            print(f'Lado mayor: {self.lado3}')
            print(f'Tipo de triangulo: Escaleno')
    #Es más ordenado, pero son más líneas.
    def caracteristicas2(self):
        if self.lado1==self.lado2==self.lado3:
            print(f'Lado mayor: {self.lado1}')
            print(f'Tipo de triangulo: Equilatero')
        elif self.lado1!=self.lado2 and self.lado1!=self.lado3:
            if self.lado1>self.lado2 and self.lado1>self.lado3:
                print(f'Lado mayor: {self.lado1}')
            elif self.lado2>self.lado1 and self.lado2>self.lado3:
                print(f'Lado mayor: {self.lado2}')
            else:
                print(f'Lado mayor: {self.lado3}')
            print(f'Tipo de triangulo: Escaleno')
        else:
            if self.lado1==self.lado2:
                if self.lado1>self.lado3:
                    print(f'Lado mayor: {self.lado1}')
                else:
                    print(f'Lado mayor: {self.lado3}')
            else:
                if self.lado1>self.lado3:
                    print(f'Lado mayor: {self.lado1}')
                else:
                    print(f'Lado mayor: {self.lado3}')
            print(f'Tipo de triangulo: Isósceles')

'''
triangulo1=Triangulo(8,3,4)
triangulo1.ladoMayor()
triangulo1.tipoTriangulo()
triangulo1.caracteristicas()
triangulo1.caracteristicas2()
print()
triangulo1=Triangulo(3,3,5)
triangulo1.ladoMayor()
triangulo1.tipoTriangulo()
triangulo1.caracteristicas()
triangulo1.caracteristicas2()
print()
triangulo1=Triangulo(3,3,3)
triangulo1.ladoMayor()
triangulo1.tipoTriangulo()
triangulo1.caracteristicas()
triangulo1.caracteristicas2()
print()
'''



'''
8) Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.
'''
class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1=numero1
        self.numero2=numero2
    def suma(self):
        return self.numero1 + self.numero2
    def resta(self):
        return self.numero1 - self.numero2
    def multiplicacion(self):
        return self.numero1 * self.numero2
    def division(self):
        return self.numero1 / self.numero2

'''
calculos=Calculadora(9,3)
print(calculos.suma())
print(calculos.resta())
print(calculos.multiplicacion())
print(calculos.division())
print(calculos.__init__(1,2))
'''

'''
9) Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones: Añadir contacto, Listar contactos, Buscar contacto, Editar contacto, Cerrar agenda.
'''
# Lo hice en un archivo separado

'''
10) En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El banco requiere también al final del día calcular la cantidad de dinero que se ha depositado. Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total. La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y deposito_total.
'''
#Cumple con lo que pide, pero no es una clase funcional real (se le debería agregar bien un menú, y poder agregar más clientes y realizar todos los cálculos con ella)
class Cliente:
    def __init__(self,nombre,cantidad):
        self.nombre=nombre
        self.cantidad=cantidad
    def depositar(self,monto):
        self.cantidad += monto
        return self.cantidad
    def extraer(self,monto):
        self.cantidad -= monto
        return self.cantidad
    def mostrar_total(self):
        return self.cantidad
    
class Banco:
    def __init__(self, cliente1, monto1, cliente2, monto2, cliente3, monto3):
        self.cliente1= Cliente(cliente1, monto1)
        self.cliente2= Cliente(cliente2, monto2)
        self.cliente3= Cliente(cliente3, monto3)
    def operar(self,cliente,monto):
        operacion=None
        while not (operacion == 1 or operacion == 2):
            operacion= int(input("""Seleccione tipo de operación: \n
                         1- Extracción\n
                         2- Depósito\n"""))
            if cliente == self.cliente1.nombre:
                if operacion == 1:
                    self.cliente1.extraer(monto)
                elif operacion == 2:
                    self.cliente1.depositar(monto)
            elif cliente == self.cliente2.nombre:
                if operacion == 1:
                    self.cliente2.extraer(monto)
                elif operacion == 2:
                    self.cliente2.depositar(monto)
            elif cliente == self.cliente3.nombre:
                if operacion == 1:
                    self.cliente3.extraer(monto)
                elif operacion == 2:
                    self.cliente3.depositar(monto)
            else:
                print('La opción ingresada no es válida')
    def deposito_total(self):
        return self.cliente1.mostrar_total() + Cliente.mostrar_total(self.cliente2) + Cliente.mostrar_total(self.cliente3)
        
        
        
banco1= Banco("Alan",150,"Daniela",100,"Lira",500)
print(banco1.deposito_total())
cliente=input('Ingrese el nombre del cliente: ')
monto= input('Ingrese el monto para la operación: ')
banco1.operar(cliente,monto)
print(f'El Monto actualizado de la cuenta es: ${banco1.cliente1.mostrar_total()}')
print(f'Los depósitos totales en el banco son de ${banco1.deposito_total()}')
