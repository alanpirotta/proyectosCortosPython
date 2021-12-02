from bicicleta import Bicicleta
from coche import Coche
from camioneta import Camioneta
from moto import Moto

def main():
    coche= Coche('rojo', 4, 55, 40)
    print(coche)
    vehiculos=[
        coche, 
        Bicicleta('rojo', 4, 'turbina'),
        Camioneta('rojo', 4, 55, 40, 1100),
        Moto('rojo', 4, 'deportiva', 160, 50)
    ]
    #Si imprimo esto directo, me muestra las ubicaciones en memoria
    # print(vehiculos)  
    print(vehiculos[0])  

    return vehiculos

    
if __name__ == '__main__':
    prueba= main()
    print(prueba[3])