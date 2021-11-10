def acronimo(cadena):
    acronimo=""
    arrayCadena= cadena.split(" ")
    for element in arrayCadena:
        acronimo+=element[0]
    
    return print(acronimo)

acronimo(input("ingrese un texto para saber el acrónimo: "))