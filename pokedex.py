import requests

def obtener_informacion_pokemon(pokemon_nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_nombre}"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos_pokemon = respuesta.json()
        
        print("Información del Pokémon:")
        print("Nombre:", datos_pokemon["name"])
        print("Altura:", datos_pokemon["height"])
        print("Peso:", datos_pokemon["weight"])
        print("Habilidades:")
        for habilidad in datos_pokemon["abilities"]:
            print("-", habilidad["ability"]["name"])
    else:
        print("No se pudo obtener la información del Pokémon.")

# Solicitar al usuario el nombre de un Pokémon
nombre_pokemon = input("Ingrese el nombre de un Pokémon: ")

# Obtener información del Pokémon
obtener_informacion_pokemon(nombre_pokemon.lower())
