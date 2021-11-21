'''
Pruebas para la agenda, diferentes formas de guardado de datos
'''
# listaContactos=[["Alan",32,"alan@alan.com"],["Daniela",34,"daniela@daniela.com"],["Melo",30,"melo@melo.com"]]
# listaContactos=["Alan","Daniela","Melo"]
'''
listaContactos=[["Alan","Daniela","Melo"],[32,34,30],["alan@ala.com","daniela@daniela.com","melo@malo.com"]]
def buscarContacto():
    busqueda= input('Nombre del contacto a buscar: ')
    resultado=listaContactos[0].index(busqueda)
    print(f'Nombre: {listaContactos[0][resultado]}')
    print(f'Edad: {listaContactos[1][resultado]}')
    print(f'Mail: {listaContactos[2][resultado]}')
    resultado= (i for i, n in enumerate(listaContactos[0]) if n == busqueda)
    for i in resultado:
        print(f'Nombre: {listaContactos[0][i]}')
        print(f'Edad: {listaContactos[1][i]}')
        print(f'Mail: {listaContactos[2][i]}')
    print('')
    print('')
buscarContacto()
'''
'''
listaContactos=[[],[],[]]
def añadirContacto():
        listaContactos[0].append(input("Ingrese el nombre del contacto: "))
        listaContactos[1].append(input("Ingrese el nombre del teléfono: "))
        listaContactos[2].append(input("Ingrese el nombre del email: "))
        listaContactos[0].append(input("Ingrese el nombre del contacto: "))
        listaContactos[1].append(input("Ingrese el nombre del teléfono: "))
        listaContactos[2].append(input("Ingrese el nombre del email: "))
        listaContactos[0].append(input("Ingrese el nombre del contacto: "))
        listaContactos[1].append(input("Ingrese el nombre del teléfono: "))
        listaContactos[2].append(input("Ingrese el nombre del email: "))
        print(listaContactos[0][0], listaContactos[1][0], listaContactos[2][0])
        print(listaContactos[0][1], listaContactos[1][1], listaContactos[2][1])
        print(listaContactos[0][2], listaContactos[1][2], listaContactos[2][2])        
añadirContacto()
'''
#Me tira loop infinito o no selecciona correctamente la opción. Solucionado
#El primer input hacía que no entrara al loop al estar fuera, y si en else ponía un input
#no entraba de nuevo.
'''
retorno=""
while not (retorno == 'no' or retorno == 'si'):
    retorno= input('Volver al menú? (si/no): ')
    if retorno == 'si':
        print("quiero volver al menú")
    elif retorno == 'no':
        print("no quiero volver al menú")
        # break
    else:
        print('La opción ingresada no es válida')
print("Salí del loop!")
'''

#class Ejemplo:
#     __atributo_privado = "Soy un atributo inalcanzable desde fuera."
# e = Ejemplo()
# print(e.__atributo_privado)

# class Ejemplo:
#     def __metodo_privado(self):
#         print("Soy un método inalcanzable desde fuera.")
# e = Ejemplo()
# e.__metodo_privado() 

class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde fuera."

    def __metodo_privado(self):
        print("Soy un método inalcanzable desde fuera.")

    def atributo_publico(self):
        return self.__atributo_privado

    def metodo_publico(self):
        return self.__metodo_privado()

e = Ejemplo()
print(e.atributo_publico())
e.metodo_publico()