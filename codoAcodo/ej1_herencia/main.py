from bicicleta import Bicicleta
from coche import Coche
from camioneta import Camioneta
from moto import Moto

def main():
    # print(coche)
    vehiculos=[
        Coche('rojo', 4, 55, 40), 
        Bicicleta('rojo', 4, 'turbina'),
        Camioneta('rojo', 4, 55, 40, 1100),
        Moto('rojo', 4, 'deportiva', 160, 50)
    ]
    #Si imprimo esto directo, me muestra las ubicaciones en memoria
    # print(vehiculos)  
    # print(vehiculos[0])  

    return vehiculos

def catalogar(articulos):
    # for clase, atributos in enumerate(articulos):
        # print(f'Clase {articulos[clase].__class__.__name__}: \nAtributos: {atributos}')
    for articulo in articulos:
        print(f'Clase: {articulo.__class__.__name__}.\nAtributos: {articulo}.')
#No estoy seguro si está mal que retorne None
        
    
if __name__ == '__main__':
    prueba= catalogar(main())
    print(prueba)