# 1) Escribe un programa muestre por pantalla “Hello World”.
# print("hello world")
# 2) Escribe un programa que escriba en la pantalla el resultado de sumar 3 + 5.
# print(3+5)
# 3) Escribe un programa que pida el nombre del usuario y escriba un texto que diga “Hola nombreUsuario”
# nombre=input("Ingrese el nombre del usuario:")
# print("Hola", nombre)
# 4) Escribe un programa que pida un número, pida otro número y escriba el resultado de sumar estos dos números.
# num1=int(input("Ingrese un numero: "))
# num2=int(input("ingrese otro numero: "))
# print(num1+num2)
# 5) Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.
# num1=int(input("Ingrese un numero: "))
# num2=int(input("ingrese otro numero: "))
# if num1>=num2:
#     print(num1)
# elif num2>num1:
#     print(num2)
# 6) Escribe un programa que pida 3 números y escriba en la pantalla el mayor de los tres.
# num1=int(input("Ingrese un numero: "))
# num2=int(input("ingrese otro numero: "))
# num3=int(input("ingrese otro numero: "))
# if num1>=num2 and num1>=num3:
#     print(num1)
# elif num2>=num1 and num2>=num3:
#     print(num2)
# elif num3>=num1 and num3>=num2:
#     print(num3)
# 7) Escribe un programa que pida un número y diga si es divisible por 2
# num1=int(input("Ingrese un numero: "))
# print(num1%2 == 0)
# 8) Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 7 (sólo hay que comprobar si lo es por uno de los cuatro)
# num1=int(input("Ingrese un numero: "))
# if num1%2 == 0 or num1%3 == 0 or num1%5 == 0 or num1%7 == 0:
#     print("el", num1, "es divisible por 2, 3, 5 o 7")
# else:
#     print("no es divisible por 2, 3, 5 ni 7")
# 9) Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible (hay que decir todos por los que es divisible)
# num1=int(input("Ingrese un numero: "))
# divisores=[2, 3, 5, 7]
# print(num1, "es divisible por: ")
# for numero in divisores:
#     if num1%numero == 0:
#         print(numero, end=", ")
#Esta forma tiene el problema de que queda la coma al final
# 10) Escribir un programa que escriba en pantalla los divisores de un número dado
# num1=int(input("Ingrese un numero: "))
# i=1
# for i in range(1,int(num1/2)+1,1):
#     # print(i)
#     if(num1%i == 0):
#         print(i, end=", ")
# print(num1, end=".")

# 11) Escribir un programa que nos diga si un número dado es primo (no es divisible por ninguno otro número que no sea él mismo o la unidad)
# num1=int(input("Ingrese un numero: "))
# divisores=[]
# i=2
# for i in range(2,int(num1/2)+1,1):
#     if(num1%i == 0):
#         divisores.append(i)
# if len(divisores) == 0:
#     print("el número es primo")
# else:
#     print("el número no es primo")

#alterno sin guardar los divisores
# num1=int(input("Ingrese un numero: "))
# primo=True
# i=2
# for i in range(2,int(num1/2)+1,1):
#     if(num1%i == 0):
#         primo=False
#         print("el número no es primo")
#         break
# if primo==True:
#     print("el número es primo")

# 12) Pide una nota (número). Muestra la calificación según la nota:
#  0-3: Muy deficiente
#  3-5: Insuficiente
#  5-6: Suficiente
#  6-7: Bien
#  7-9: Notable
#  9-10: Sobresaliente
# nota = float(input("Ingrese su nota: "))
# if 0<= nota <= 3:
#     print("Muy deficiente")
# elif 3< nota <= 5:
#     print("Insuficiente")
# elif 5< nota <= 6:
#     print("Suficiente")
# elif 6< nota <= 7:
#     print("Bien")
# elif 7< nota <= 9:
#     print("Notable")
# elif 9< nota <= 10:
#     print("Sobresaliente")

# 13) Realiza un programa que escriba una pirámide del 1 al 30 de la siguiente forma:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# ……….
# largoPiramide=int(input("Ingrese de cuantas filas se hará la pirámide: "))
# for num in range(1,largoPiramide+1):
#     for i in range(1,num):
#         print(num, end="")
#     print(num)
# #     print("estoy fuera del primer loop")
# # print("estoy fuera del loop")


# 14) Haz un programa que escriba una pirámide inversa de los números del 1 al número que indique el usuario de la siguiente forma (suponiendo que indica 6):
# 666666
# 55555
# 4444
# 333
# 22
# 1
# largoPiramide=int(input("Ingrese de cuantas filas se hará la pirámide: "))
# for num in range(largoPiramide,0,-1):
#     for i in range(1,num):
#         print(num, end="")
#     print(num)

# 15) Crear un programa que escriba los números del 1 al 500, y que indique cuales son múltiplos de 4 y de 9 y que cada 5 líneas muestre una línea horizontal. Por ejemplo:
# 1
# 2
# 3
# 4 (Múltiplo de 4)
# 5
# ------------------------------------------------------------
# 6
# 7
# 8 (Múltiplo de 4)
# 9 (Múltiplo de 9)
# 10
# for i in range(1,501):
#     if i%4 == 0 and i%9 == 0:
#         print(i, "(Múltiplo de 4) (Múltiplo de 9)")
#     elif i%4 == 0:
#         print(i, "(Múltiplo de 4)")
#     elif i%9 == 0:
#         print(i, "(Múltiplo de 9)")
#     else:
#         print(i)
#     if i%5 == 0:
#         print("-----------------------------------")