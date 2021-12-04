from bicicleta import Bicicleta
from coche import Coche
from camioneta import Camioneta
from moto import Moto

def main():
    # print(coche)
    vehiculos=[
        Coche('rojo', 4, 55, 40), 
        Bicicleta('rojo', 2, 'turbina'),
        Camioneta('rojo', 6, 55, 40, 1100),
        Moto('rojo', 2, 'deportiva', 160, 50)
    ]
    #Si imprimo esto directo, me muestra las ubicaciones en memoria
    # print(vehiculos)  
    # print(vehiculos[0])  

    return vehiculos

def catalogar(articulos, ruedas=-1):
    # for clase, atributos in enumerate(articulos):
        # print(f'Clase {articulos[clase].__class__.__name__}: \nAtributos: {atributos}')
    contador=0
    if ruedas == -1:
        for articulo in articulos:
            print(f'Clase: {articulo.__class__.__name__}.\nAtributos: {articulo}.')
    else:
        for articulo in articulos:
            if articulo.ruedas == ruedas:
                print(f'Clase: {articulo.__class__.__name__}.\nAtributos: {articulo}.')
                contador+=1
        print('Se han encontrado {} vehículos con {} ruedas:'.format(contador,ruedas))
        
    
if __name__ == '__main__':
    prueba= catalogar(main(),2)