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