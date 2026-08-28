import json

def create_new_pokemon():

    name = input("Agregue el nombre del pokemon: ")
    pokemon_type = input("Ingrese el tipo de pokemon: ")

    while True:
        try:
            level = int(input("Ingrese el nivel del pokemon: "))
            break
        except ValueError:
            print("Debes ingresar un numero")
    while True:
        try: 
            weight = float(input("Ingrese el peso del pokemon: "))
            break
        except ValueError:
            print("Debes ingresar un numero")
    
    while True:
        shiny_type = input("¿El Pokémon es shiny? (si/no): ")

        if shiny_type == "si":
            is_shiny = True
            break

        elif shiny_type == "no":
            is_shiny = False
            break
        else: 
            print("Ingresa un 'si' o 'no'")

    new_pokemon = {
    "name": name,
    "type": pokemon_type,
    "level": level,
    "weight_kg": weight,
    "is_shiny": is_shiny
    }

    return new_pokemon


def new_pokemon_json(json_file):
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            pokemons = json.load(file)

    except FileNotFoundError:
        print("No se encontró el archivo.")
        return

    except json.JSONDecodeError:
        print("El archivo JSON está vacío o tiene un formato incorrecto.")
        return
    new_pokemon = create_new_pokemon()

    pokemons.append(new_pokemon)

    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(pokemons, file, indent=4, ensure_ascii=False)

def main():

    new_pokemon_json('pokemons.json')

if __name__ == "__main__":

    main()