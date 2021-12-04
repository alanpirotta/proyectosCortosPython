#Podría modificar para que en las búsquedas funcione para mayúsculas y minúsculas.
class Agenda:

    def __init__(self):
        self.listaContactos=[[],[],[],[]]
        self.abierta=False
        self.id=1

    #Menú distribuidor para las demás funciones
    def menu(self):
        self.abierta=True
        choice=""
        # while(choice != "5"):
        while self.abierta == True:
            print("--------------")
            print("Seleccione una opción")
            print("--------------")
            print("1-Añadir contacto")
            print("2-Listar contactos")
            print("3-Buscar contactos")
            print("4-Editar contacto")
            print("5-Cerrar agenda")
            choice=input("Opción: ")
            if choice == "1":
                self.añadirContacto()
            elif choice == "2":
                self.listarContactos()
            elif choice == "3":
                self.buscarContacto()
            elif choice == "4":
                self.editarContacto()
            elif choice == "5":
                self.cerrarAgenda()
                continue
            else:
                print("La opción ingresada no es válida")
            retorno=""
            while not retorno == 'no' or retorno == 'si':
                retorno= input('Volver al menú? (si/no): ')
                if retorno == 'si':
                    break
                elif retorno == 'no':
                    self.cerrarAgenda()                        
                else:
                    print('La opción ingresada no es válida')

    def añadirContacto(self):
        self.listaContactos[0].append(self.id)
        self.id+=1
        self.listaContactos[1].append(input("Ingrese el nombre del contacto: "))
        self.listaContactos[2].append(input("Ingrese el número de teléfono: "))
        self.listaContactos[3].append(input("Ingrese el email: "))

    def listarContactos(self):
        for i in range(len(self.listaContactos[0])):
            print("")
            print(f'Id: {self.listaContactos[0][i]}')
            print(f'Nombre: {self.listaContactos[1][i]}')
            print(f'Teléfono: {self.listaContactos[2][i]}')
            print(f'Mail: {self.listaContactos[3][i]}')

    def buscarContacto(self):
        busqueda= input('Nombre del contacto a buscar: ')
        #Permite encontrar y mostrar si hay más de uno con el mismo nombre, pero no puedo
        #traerlo después para poder editarlo.
        resultado= (i for i, n in enumerate(self.listaContactos[1]) if n == busqueda)
        for i in resultado:
            print('')
            print(f'Id: {self.listaContactos[0][i]}')
            print(f'Nombre: {self.listaContactos[1][i]}')
            print(f'Edad: {self.listaContactos[2][i]}')
            print(f'Mail: {self.listaContactos[3][i]}')
        #Este sólo encuentra el primero, si hay repetido falla
        '''
        resultado=self.listaContactos[0].index(busqueda)
        print(f'Nombre: {self.listaContactos[0][resultado]}')
        print(f'Edad: {self.listaContactos[1][resultado]}')
        print(f'Mail: {self.listaContactos[2][resultado]}')
        '''

    def editarContacto(self):
        self.buscarContacto()
        eleccion=int(input('Cuál es el ID del contacto a modificar?: '))
        self.listaContactos[2][eleccion-1]=input('Ingrese el nuevo número de teléfono: ')
        self.listaContactos[3][eleccion-1]=input('Ingrese el nuevo mail: ')

    def cerrarAgenda(self):
        self.abierta=False
        print("La agenda se ha cerrado")


agendaAlan=Agenda()
agendaAlan.menu()
