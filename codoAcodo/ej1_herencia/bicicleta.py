from vehiculo import Vehiculo 

class Bicicleta(Vehiculo):
    
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        if tipo == 'turbina' or tipo == 'deportiva':
            self.tipo=tipo
        else:
            print('no es un tipo válido de bicicleta')
    
    def __str__(self) -> str:
        return super().__str__() + f' Tipo: {self.tipo}'
              
              
if __name__ == '__main__':
    #Depende como se ingrese el dato, se le pide antes, y se le da opción de sólo esos dos tipos
    bicicleta=Bicicleta('rojo', 4, 'turbina')
    print(bicicleta)
