adjective1 = input("Ingrese un adjetivo: ")
name1 = input("Ingrese un nombre: ")
verb1 = input("Ingrese un verbo en tercera persona: ")
noun1 = input("Ingrese un sustantivo: ")

print(adjective1, name1, verb1, noun1, end="")
print("")

#método dos
text=f"""{adjective1} {name1} {verb1} {noun1}"""

print(text)

#método tres
text2="""{} {} {} {}"""

print(text2.format(adjective1, name1, verb1, noun1))

#Formas de hacerlo más complejo. Generar una historia de varios renglones, también puedo agregarles texto propio para guiar la historia, los  tres métodos sirven
#las llaves vacías del método 3, se les puede asignar nombre, y agregarlo en el format()


