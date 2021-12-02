from bicicleta import Bicicleta 

class Moto(Bicicleta):
    
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    
    def __str__(self) -> str:
        return super().__str__() + f' Velocidad: {self.velocidad}km/h. Cilindrada: {self.cilindrada}cc'
              
              
if __name__ == '__main__':
    #Depende como se ingrese el dato, se le pide antes, y se le da opción de sólo esos dos tipos
    moto=Moto('rojo', 4, 'turbina', 100, 50)
    print(moto)
