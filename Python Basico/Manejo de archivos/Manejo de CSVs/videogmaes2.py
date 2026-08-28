import csv

def save_games_info(file):

    while True:
        try:
            amount = int(input("¿Cuántos videojuegos desea ingresar?: "))
            if amount <= 0:
                print("Debe ingresar una cantidad mayor que 0.")
                continue
            break

        except ValueError:
            print("Debe ingresar un número entero.")
            
    with open(file, 'w', encoding='utf-8', newline='') as csv_file:
        
        fieldnames = ["nombre", "genero", "desarrollador", "clasificacion"]

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='\t')

        writer.writeheader()

        for number in range(amount):
            print(f"\n--- Videojuego {number + 1} ---")
            name = input("Ingrese el nombre del videojuego: ")
            gender = input("Ingrese el género: ")
            developer = input("Ingrese el desarrollador: ")
            classification = input("Ingrese la clasificación ESRB: ")

            game = {
                "nombre": name,
                "genero": gender,
                "desarrollador": developer,
                "clasificacion": classification
                }

            writer.writerow(game)


def main():

    save_games_info('video_games_data.csv')

if __name__ == "__main__":

    main()