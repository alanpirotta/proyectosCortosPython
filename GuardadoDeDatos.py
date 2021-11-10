#Acá sólo la está imprimiendo, pero podría guardar las variables en algún lugar u objeto

def userData():
    name=input("Cual es tu nombre? ")
    while name.isdigit() == True:
        name=input("Ingrese un nombre válido: ")  
    age=input("Cual es tu edad? ")
    while age.isdigit() == False:
        age=input("Ingrese una edad válida: ")
    mail=input("Cual es tu mail? ")
    # while(mail.find("@") == -1):  #alternativa descartada
    while("@" not in mail):     
        mail=input("Ingrese un mail válido: ")
    phone=input("Cual es tu teléfono? ")
    while phone.isdigit() == False:
        phone=input("Ingrese un teléfono válido: ")
    return print(f'''Su información es:
                    Nombre: {name}
                    edad: {age}
                    mail: {mail}
                    teléfono: {phone} 
                    ''')

userData()