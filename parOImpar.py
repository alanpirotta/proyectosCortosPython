def parImpar(num):
    if num == 0:
        return "El número es cero"
    elif num%2 == 0:
        return "El número es par"
    elif num%2 == 1:
        return "El número es impar"
    else:
        return "el parámetro no es un número"
    
resultado = parImpar(13543215342) #poner el número que se quiere probar
print(resultado)

        
        
    