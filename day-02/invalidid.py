import sys

def validate_id(path):
    try:
        with open(path, 'r', encoding='utf-8') as archivo:
            inicialarray = archivo.read().split(",")

            for element in inicialarray:
                actualelement = element.split("-")
                actualarray = list(range(int(actualelement[0]), int(actualelement[1])+1))
            return 0

    except FileNotFoundError:
        print(f"Error: El archivo '{id}' no se encontró.")
        return False
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python invalidid.py <ruta_del_archivo>")
        sys.exit(1)

    path = sys.argv[1]
    es_valido = validate_id(path)