'''
Desarrollar una función que reciba tres números positivos y devuelva el mayor de los tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar también un programa para ingresar los tres valores, invocar a la función y mostrar el máximo hallado, o un mensaje informativo si éste no existe.
'''
'''
def numeroMayor(num1, num2, num3):
    if len([num1, num2, num3]) == len(set([num1,num2,num3])):
         return max(num1,num2,num3)
    else:
        return "los valores no son únicos"
    
num1 = int(input("Ingrese un valor positivo: "))
if num1 < 0:
    print("no es un número positivo")
    num1= int(input("Ingrese un número positivo: "))
num2 = int(input("Ingrese otro valor positivo: "))
if num2 < 0:
    print("no es un número positivo: ")
    num2= int(input("Ingrese un número positivo: "))
num3 = int(input("Ingrese otro valor positivo: "))
if num3 < 0:
    print("no es un número positivo")
    num3= int(input("Ingrese un número positivo: "))

resultado = numeroMayor(num1, num2, num3)
print(resultado)
'''

'''
Desarrollar una función que reciba tres números enteros positivos y verifique si corresponden a una fecha válida (día, mes, año). Devolver True o False según la fecha sea correcta o no. Realizar también un programa para verificar el comportamiento de la función.
'''
'''
def esFechaValida(dia, mes, año):
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        if dia<=31:
            return True
        else:
            return False
    elif mes==4 or mes==6 or mes==9 or mes==11:
        if dia<=30:
            return True
        else:
            return False
    elif mes==2:
        if año%4 == 0:
            if dia <=29:
                return True
            else:
                return False
        else:
            if dia <=28:
                return True
            else:
                return False
    else:
        return False
        
dia = int(input("Ingrese un día: "))
if dia <= 0:
    print("no es un día")
    dia= int(input("Ingrese un día: "))
mes = int(input("Ingrese un mes: "))
if mes <= 0:
    print("no es un mes: ")
    mes = int(input("Ingrese un mes: "))
año = int(input("Ingrese un año: "))
if año <= 0:
    print("no es un año")
    año = int(input("Ingrese un año: "))

resultado = esFechaValida(dia, mes, año)
print(resultado)
'''


'''
Un comercio de electrodomésticos necesita para su línea de cajas un programa que le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan dos números enteros, correspondientes al total de la compra y al dinero recibido. Informar cuántos billetes de cada denominación deben ser entregados al cliente como vuelto, de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir un mensaje de error si el dinero recibido fuera insuficiente. Ejemplo: si la compra es de $317 y se abona con $500, el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete de $20, 1 billete de $10 y 3 billetes de $1.
'''
'''
def cambio(costo, pagado):
    vuelto = costo - pagado
    billete500 = 0
    billete100 = 0
    billete50 = 0
    billete20 = 0
    billete10 = 0
    billete5 = 0
    billete1 = 0
    if vuelto < 0:
        return print("El dinero es insuficiente")
    else:
        while vuelto > 500:
            billete500+=1
            vuelto -= 500
        while vuelto > 100:
            billete100+=1
            vuelto -= 100
        while vuelto > 50:
            billete50 += 1
            vuelto -= 50
        while vuelto > 20:
            billete20 += 1
            vuelto -= 20
        while vuelto > 10:
            billete10 += 1
            vuelto -= 10
        while vuelto > 5:
            billete5 += 1
            vuelto -= 5
        while vuelto > 1:
            billete1 += 1
            vuelto -= 1
    return print(f'Su vuelto es ${costo-pagado}. Dar de vuelto {billete500} billetes de $500, {billete100} billetes de $100, {billete50} billetes de $50, {billete20} billetes de $20, {billete10} billetes de $10, {billete5} billetes de $5 y {billete1} billetes de $1')
   
resultado= cambio(500,317)
'''
#Funcionó, pero quiero probar con listas y un eliminar cuando son 0 billetes


'''
def cambio (costo, pagado):
    vueltoRestante = pagado - costo
    billetes = [500, 100, 50, 20, 10, 5, 1]
    cantidadBilletes = [0,0,0,0,0,0,0]
    cambio= f'Su vuelto es {vueltoRestante}. Devolver '
    if vueltoRestante < 0:
        return "Lo pagado no es suficiente"
    else:
        for i in range(7):
            while vueltoRestante > billetes[i]:
                vueltoRestante -= billetes[i]
                cantidadBilletes[i] += 1
            if cantidadBilletes[i] == 0:
                continue
            elif cantidadBilletes[i] == 1:
                cambio += f'{cantidadBilletes[i]} billete de ${billetes[i]}, '
            else:
                cambio += f'{cantidadBilletes[i]} billetes de ${billetes[i]}, '       
        cambio = cambio.strip(", ")
        return cambio
            
            
resultado = cambio(100,318)
print(resultado)
'''

'''
Escribir dos funciones separadas para imprimir por pantalla los siguientes patrones de asteriscos, donde la cantidad de filas se recibe como parámetro:
**********          **
**********          ****
**********          ******
**********          ********
**********          **********
'''
'''
def patronLineal(filas):
    for i in range(filas):
        print("**********")
        
def patronAumentaEnDos(filas):
    for i in range(filas):
        for j in range((i+1)*2):
            print("*", end="")
        print("")

        
patronLineal(7)

patronAumentaEnDos(10)
'''

'''
Crear una función lambda que devuelva el cuadrado de un valor recibido cómo parámetro. Desarrollar además un programa para verificar el comportamiento de la función.
'''
'''
cuadrado = lambda x: x**2
print(cuadrado(12))
'''

'''
Crear una función lambda para comprobar si un número es par o impar. Desarrollar además un programa para verificar el comportamiento de la función.
'''
'''
par = lambda x: True if x%2 == 0 else False
print(par(1126457892010))
'''

'''
7) Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista.
'''

'''
def listaCuadrados(N):
    listaCuadrados=[]
    for i in range(1,N+1):
        listaCuadrados.append(i**2)
    return listaCuadrados

def imprimirUltimos10(lista):
    ultimosDiez = []
    for i in range(-10,-1):
        ultimosDiez.append(lista[i])
    print('Los últimos diez números de la lista son:', ultimosDiez)

imprimirUltimos10(listaCuadrados(20))
'''

'''
8) Eliminar de una lista de palabras que se encuentren en una segunda lista. Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.
'''

'''
lista = ["hola", "chau", "Alan", "Pedro", "Ana", "Daniela", "Carlos"]
print(lista)
listaPalabrasAEliminar = ["Alan", "chau", "Juan", "Ana"]
print(listaPalabrasAEliminar)
for element in listaPalabrasAEliminar:
    if element in lista:    #Si no hago esto, tira error con palabras que no están
        lista.remove(element) 
print(lista)
'''

#Tiene un conflicto si la lista original tiene duplicados, sólo elimina el primero.

#alternativa
'''
lista = ["hola", "chau", "Alan", "Pedro", "Ana", "Daniela", "Carlos", "Alan"]
print(lista)
listaPalabrasAEliminar = ["Alan", "chau", "Juan", "Ana"]
print(listaPalabrasAEliminar)
listaNueva = []
for element in lista:
    listaNueva.append(element)
#recorró la lista origina, eliminando de la segunda (evito el salto del siguiente elemento al eliminar el actual) 
for element in lista: 
    if element in listaPalabrasAEliminar:   
        listaNueva.remove(element) 
print(listaNueva)
'''


'''
9) Escribir una función que reciba una lista como parámetro y devuelva True si la lista está ordenada en forma ascendente o False en caso contrario. Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar además un programa para verificar el comportamiento de la función.
'''
'''
def ordenadaAscendente(lista):
    return lista == sorted(lista)

resultado = ordenadaAscendente([5,4,8,9,1,2])
print(resultado)
resultado2 = ordenadaAscendente([1,5,25,98,15631])
print(resultado2)
'''

'''
10) Desarrollar una función que determine si una cadena de caracteres es capicúa, sin utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita verificar su funcionamiento.
'''
'''
def capicua(cadena): #Tengo que probar hacer un ciclo que recorra todas las posiciones de los caracteres y lo compare contra los opuestos
    j = -1
    capicua = True
    for i in range(len(cadena)):
        # print(f'valor i {i}, valor j {j}')
        # print(f'{cadena[i]} es igual a {cadena[j]}')
        if cadena[i] != cadena[j]:
            capicua = False
            break
        j -= 1
    return capicua
    #no funciona esto de abajo, después tengo que ver el error  y averiuar por qué ocurre
    #return cadena.split("").join("") == cadena.split("").reversed().join("")
resultado = capicua("neuquen")
print(resultado)
resultado2 = capicua("hola me llamo alan nala omall em aloh")
print(resultado2)
resultado3 = capicua("oihsalkfhds")
print(resultado3)
'''

'''
11) Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la misma tiene 80 columnas.
'''
'''
cadena="hola me llamo alan"
print(cadena.center(80))
'''

'''
12) Escribir una función que reciba como parámetro una tupla conteniendo una fecha (día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada en formato extendido. Por ejemplo, para (12, 10,17) devuelve “12 de Octubre de 2017”. Escribir también un programa para verificar su comportamiento.
'''
'''
def fechaExtendida (tupla):
    mes = ""
    if tupla[1] < 1 or tupla[1] > 12:
        return "no es una fecha válida" #podría chequear que sea fecha válida usando la función de la línea 32
    elif tupla[1] == 1:
        mes= "Enero"
    elif tupla[1] == 2:
        mes= "Febrero"
    elif tupla[1] == 3:
        mes= "Marzo"
    elif tupla[1] == 4:
        mes= "Abril"
    elif tupla[1] == 5:
        mes= "Mayo"
    elif tupla[1] == 6:
        mes= "Junio"
    elif tupla[1] == 7:
        mes= "Julio"
    elif tupla[1] == 8:
        mes= "Agosto"
    elif tupla[1] == 9:
        mes= "Septiembre"
    elif tupla[1] == 10:
        mes= "Octubre"
    elif tupla[1] == 11:
        mes= "Noviembre"
    elif tupla[1] == 12:
        mes= "Diciembre"
    return f'{tupla[0]} de {mes} de {tupla[2]}'

resultado = fechaExtendida((30, 11, 1988))
print(resultado)
resultado2 = fechaExtendida((31, 12, 2021))
print(resultado2)
'''

'''
13) Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras ordenadas según su longitud.
'''
'''
frase = input("ingrese una frase: ")
listaFrase = sorted(list(set(frase.split(" "))), key = len)
print(listaFrase)
'''


'''
14) Desarrollar una función eliminar_claves() que reciba como parámetros un diccionario y una lista de claves. La función debe eliminar del diccionario todas las claves contenidas en la lista, devolviendo el diccionario modificado y un valor de verdad que indique si la operación fue exitosa. Desarrollar también un programa para verificar su comportamiento.
'''
'''
def eliminar_claves(diccionario, claves):
    for clave in claves:
        if clave in diccionario:
            # diccionario.pop(clave) #Alternativa, funcionan igual
            del diccionario[clave]

diccionario = {'saludo': 'hola', 'nombre': 'Alan', 'Apellido': 'Pirotta', 'edad' : 32}
print(diccionario)
eliminar_claves(diccionario, ['saludo', 'edad'])
print(diccionario)
'''

'''
15) Escribir una función para eliminar una subcadena de una cadena de caracteres, a partir de una posición y cantidad de caracteres dados, devolviendo la cadena resultante. Escribir también un programa para verificar el comportamiento de la misma. Escribir una función utilizando rebanadas.
'''

'''
def eliminarSubcadena(cadena, posicion, cantidad):
    if posicion < 0 or posicion > len(cadena)-1:
        return "La posición no es válida"
    listaCadena = list(cadena)
    del listaCadena[int(posicion):int((posicion+cantidad))]
    cadenaCortada = ''.join(listaCadena)
    return cadenaCortada
'''

#Alternativa sin pasar a una lista
'''
def eliminarSubcadena(cadena, posicion, cantidad):
    if posicion < 0 or posicion > len(cadena)-1:
        return "La posición no es válida"
    subString = cadena[int(posicion):int(cantidad+posicion)]
    cadenaCortada= cadena.replace(subString,"")
    return cadenaCortada
    
    
resultado = eliminarSubcadena("hola me llamo Alan", 18, 1)
print(resultado)
'''