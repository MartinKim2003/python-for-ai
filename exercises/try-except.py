"""
1) Modificá tu función get_weather para que si la API falla o no devuelve el dato, 
no rompa el programa sino que imprima "No se pudo obtener el clima para esta ciudad".
"""
import requests

def get_weather(latitude, longitude):
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
        response = requests.get(url)
        data = response.json()
        return data["current"]["temperature_2m"]
    except Exception as e:
        print("Hubo un fallo con el request de la API")

paris_temp = get_weather("48.84", "2.36")
print(f"La temperatura actual de paris es de: {paris_temp} °C")

"""
Ejercicio 2
Creá una función dividir(a, b) que divida dos números. Si el usuario pasa 0 como divisor, que capture el error y 
devuelva "No se puede dividir por cero" en vez de romperse.
"""
def division(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        print("No se puede poner un 0 como denominador")

resultado = division(10,2)
print(resultado)

"""
Ejercicio 3
Creá una clase Ciudad con:

Atributos: nombre, latitud, longitud
Un método describir() que imprima "Ciudad: Buenos Aires | Lat: -34.60 | Lon: -58.38"

Creá 2 instancias con ciudades distintas y llamá a describir() en cada una.
"""

class Ciudad:
    def __init__(self, nombre, latitud, longitud):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        
    def describir(self):
        print(f"Ciudad: {self.nombre} | Lat: {self.latitud} | Lon: {self.longitud}")
        

ciudad1 = Ciudad("Buenos Aires", "-34.60","-58.3" )
ciudad2 = Ciudad("Paris","48.85", "2.35")
ciudad1.describir()
ciudad2.describir()

"""
Ejercicio 4
Agregale a la clase Ciudad un método get_temperatura() que llame a tu función get_weather y devuelva la temperatura actual de esa ciudad.
"""
class Ciudad:
    def __init__(self, nombre, latitud, longitud):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        
    def describir(self):
        print(f"Ciudad: {self.nombre} | Lat: {self.latitud} | Lon: {self.longitud}")
    
    def get_weather(self):       
        url = f"https://api.open-meteo.com/v1/forecast?latitude={self.latitud}&longitude={self.longitud}&current=temperature_2m"
        response = requests.get(url)
        data = response.json()
        return data["current"]["temperature_2m"]            
        

ciudad1 = Ciudad("Buenos Aires", "-34.60","-58.3" ) # con esto defino mi primer objeto de "Ciudad" 
ciudad2 = Ciudad("Paris","48.85", "2.35") # con esto defino mi segund objeto de Ciudad
ciudad1_temp = ciudad1.get_weather() # con esto obtengo la temperatura de la ciudad de Buenos Aires
ciudad1.describir() # con esto obtengo una breve descripción de la ciudad de Buenos Aires
ciudad2.describir() # con esto obtengo una breve descripción de la ciudad de Paris


"""
Ejecicio 5: Combinado
Juntá todo: creá una lista con 3 instancias de Ciudad, recorrela con un loop, llamá a get_temperatura() en cada una, 
y usá try-except para que si alguna falla el loop siga con la siguiente.
"""

ciudades = [
    Ciudad("Buenos Aires", -34.60, -58.38),
    Ciudad("Paris", 48.85, 2.35),
    Ciudad("Tokyo", 35.68, 139.69)
]

for ciudad in ciudades:
    try:
        temperatura_ciudad = ciudad.get_weather()
        print(f"La temeperatura de {ciudad.nombre} es: {temperatura_ciudad} °C")
    except Exception as e:
        print("Hubo un fallo dentro del programa ")