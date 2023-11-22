class Auto:
    def __init__(self, patente, precio, color, modelo, marca, aro_ruedas, motor, potencia, id:int=0):
        self.__patente = patente
        self.__precio = precio
        self.__color = color
        self.__modelo = modelo
        self.__marca = marca
        self.__aro_ruedas = aro_ruedas
        self.__motor = motor
        self.__potencia = potencia

    def get_patente(self):
        return self.__patente
    def set_patente(self, patente):
        self.__patente = patente

    def get_precio(self):
        return self.__precio
    def set_precio(self, precio):
        self.__precio = precio

    def get_color(self):
        return self.__color
    def set_color(self, color):
        self.__color = color

    def get_modelo(self):
        return self.__modelo
    def set_modelo(self, modelo):
        self.__modelo = modelo

    def get_marca(self):
        return self.__marca
    def set_marca(self, marca):
        self.__marca = marca

    def get_aro_ruedas(self):
        return self.__aro_ruedas
    def set_aro_ruedas(self, aro_ruedas):
        self.__aro_ruedas = aro_ruedas

    def get_motor(self):
        return self.__motor
    def set_motor(self, motor):
        self.__motor = motor

    def get_potencia(self):
        return self.__potencia
    def set_potencia(self, potencia):
        self.__potencia = potencia
    
    def set_id(self, id:int):
        self.__id = id
            
    def __str__(self):
        txt = f"ID: {self.__id}"
        txt += f"\nPatente: {self.__patente}"
        txt += f"\nPrecio: {self.__precio}"
        txt += f"\nColor: {self.__color}"
        txt += f"\nModelo: {self.__modelo}"
        txt += f"\nMarca: {self.__modelo}"
        txt += f"\nAro de ruedas: {self.__modelo}"
        txt += f"\nMotor: {self.__modelo}"
        txt += f"\nPotencia: {self.__modelo}"
        return txt

