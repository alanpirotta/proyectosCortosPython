'''
1) Crear la clase Persona con los métodos “set_nombre”, “set_edad”, “get_nombre”, “get_edad” y “print_persona”. Luego crear dos objetos del tipo Persona e imprimirlos por consola.
'''
class Persona:
    nombre = ""
    edad = ""
    #ej 2
    def inicializar(self, nom, e):
        self.nombre=nom
        self.edad=e
        
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
        if self.edad > persona:
            return True
        else:
            return False

    @staticmethod
    def get_mayor(persona1,persona2):
        if persona1 == persona2:
            return "las dos personas tienen la misma edad"
        elif persona1 > persona2:
            return persona1
        else:
            return persona2
        
            
    #Método para impimir los datos, no es necesario
    # def imprimir(self):
    #     print(f'Nombre: {self.nombre}. Edad: {self.edad}')
    
persona1 = Persona()
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
persona2=Persona()
persona2.inicializar("Juan", 40)
print(persona2.get_nombre(), persona2.get_edad())
'''
3) Agregarle a la clase anterior un método “es_mayor_de_edad” que devuelva True o False.
'''
print(persona1.mayor_de_edad())
print(persona2.mayor_de_edad())

'''
4) Agregarle un método “es_mayor_que” el cual recibe un objeto persona y compara su edad con la del objeto actual.
'''
print("es mayor que", persona2.es_mayor_que(persona1.edad)) 

'''
5) Agregarle un método estático “get_mayor” que reciba dos objetos Persona y devuelva el de edad mayor.
'''
print(Persona.get_mayor(persona1.edad, persona2.edad))
#está mal esto y el anterior
'''
6) Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.´
'''

'''
7) Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno).
'''

'''
8) Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.
'''

'''
9) Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones: Añadir contacto, Listar contactos, Buscar contacto, Editar contacto, Cerrar agenda.
'''

'''
10) En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El banco requiere también al final del día calcular la cantidad de dinero que se ha depositado. Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total. La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y deposito_total.
'''