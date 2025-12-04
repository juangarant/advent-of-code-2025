import sys

def is_repetition_list(seq):
    n = len(seq)
    if n%2 != 0:
        return False, None
        
    mitad = n // 2

    return seq[:mitad] == seq[mitad:], None

def validate_id(path):
    try:
        with open(path, 'r', encoding='utf-8') as archivo:
            inicialarray = archivo.read().split(",")
            total = 0
            for element in inicialarray:
                actualelement = element.split("-")
                actualarray = list(range(int(actualelement[0]), int(actualelement[1])+1))
                for i in actualarray:
                    realactualarray = list(map(int, str(i)))
                    if is_repetition_list(realactualarray)[0]:
                        print(f"El ID {i} es inválido debido a repeticiones.")
                        total += i
                
            return total

    except FileNotFoundError:
        print(f"Error: El archivo '{id}' no se encontró.")
        return False
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python invalidid.py <ruta_del_archivo>")
        sys.exit(1)

    path = sys.argv[1]
    es_valido = validate_id(path)
    if es_valido is not False:
        print(f"Suma de IDs inválidos: {es_valido}")