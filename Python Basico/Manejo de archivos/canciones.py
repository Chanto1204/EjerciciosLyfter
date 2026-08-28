def save_file(songs, songs2):
    try:
        with open(songs, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        lines.sort()

        with open(songs2, 'w', encoding='utf-8') as file2:
            for line in lines:
                if line.endswith('\n'):
                    file2.write(line)
                else:
                    file2.write(line + '\n') 
        for number, line in enumerate(lines, start=1):
            print(f"{number} - {line.strip()}")

    except FileNotFoundError:
        print("No se encontró el archivo")

def main():
    songs = input("Ingrese el nombre del archivo a leer: ")
    songs2 = input("Ingrese el nombre del archivo donde desea guardar las canciones: ")

    save_file(songs, songs2)


if __name__ == "__main__":
    main()