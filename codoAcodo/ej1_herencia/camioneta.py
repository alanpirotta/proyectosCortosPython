from coche import Coche 

class Camioneta(Coche):
    
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga=carga
        
    def __str__(self) -> str:
        return super().__str__() + f' Carga: {self.carga}kg'
              
              
if __name__ == '__main__':
    camioneta=Camioneta('rojo', 4, 55, 40, 1000)
    print(camioneta)
