from Auto import Auto
from Dao import Dao



#patente, precio, color, modelo, marca, aro_ruedas, motor, potencia,
def RegistrarAuto():
    patente = input("Ingresa patente del auto: ")
    precio = input("Ingresa precio del auto: ")
    color = input("Ingresa patente del auto: ")
    modelo = input("Ingresa patente del auto: ")
    marca = input("Ingresa patente del auto: ")
    aro_ruedas = input("Ingresa patente del auto: ")
    motor = input("Ingresa patente del auto: ")
    potencia = input("Ingresa patente del auto: ")
    a = Auto(patente, color, precio, modelo, marca, aro_ruedas, potencia, motor)
    d = Dao()
    d = RegistrarAuto(a)

def MostrarAutos():
    pass

def ModificarAuto():
    pass

def EliminarAuto():
    pass

def MostrarAutosMismoColor():
    pass

def MostrarAutoPorPatente():
    pass

def Menu():
    print("----Menu----")
    print("1: Registrar Auto ")
    print("2: Modificar Auto ")
    print("3: Eliminar Auto ")
    print("4: Mostrar Autos ")
    print("5: Buscar Auto por patente ")
    print("6: Mostrar Autos que tengan el mismo color ")
    print("7: Detener Programa ")
    opcion = input("ingresa una opcion: ")

    if opcion =="1":
        RegistrarAuto()
    elif opcion =="2":
        ModificarAuto()
    elif opcion == "3":
        MostrarAutos()
    elif opcion == "4":
        EliminarAuto()
    elif opcion =="5":
        MostrarAutoPorPatente()
    elif opcion =="6":
        MostrarAutosMismoColor()
    elif opcion =="7":
        return True
    else:
        print("opcion no valida")

while Menu()!=True:
    pass
