class Vehiculo():
    def __init__(self, color, ruedas):
        self.color=color
        self.ruedas=ruedas
    
    def __str__(self) -> str:
        return f'Color: {self.color}. Ruedas: {self.ruedas}.'
        

if __name__ == '__main__':
    vehiculo=Vehiculo('rojo', 4)
    print(vehiculo)