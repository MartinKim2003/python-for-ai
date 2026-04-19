import requests
# Ejercicio 1

numeros = [3, 15, 7, 22, 8, 11]

def mayor_10(lista):
    nueva_lista = []
    for i in lista:
        if i > 10:
            nueva_lista.append(i)
    
    return nueva_lista

lista_mayor10 = mayor_10(numeros)
print(lista_mayor10)

# Ejercicio 2
ciudades = {
    "Buenos Aires": 3000000,
    "Córdoba": 1400000,
    "Rosario": 900000,
    "Mendoza": 800000
}

for ciudad, habitantes in ciudades.items():
    if habitantes > 1000000:
        print(f"La ciudad {ciudad} con {habitantes:,} habitantes")
    
ciudades = {
    "Buenos Aires": (-34.90, -58.38),
    "Paris": (48.85, 2.35),
    "Londres": (51.50, -0.12),
    "Tokio": (35.68, 139.69)
}

for ciudad in ciudades:
    print(ciudad)
    
for ciudad, coordenadas in ciudades.items():
    print(f"{ciudad} esta ubicado en {coordenadas}")
    
for ciudad, coordenadas in ciudades.items():
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={coordenadas[0]}&longitude={coordenadas[1]}&current=temperature_2m,relative_humidity_2m,wind_speed_10m")
    data = response.json()
    temperatura = (data["current"]["temperature_2m"])
    print(f"La temperatura en {ciudad} es de {temperatura}")