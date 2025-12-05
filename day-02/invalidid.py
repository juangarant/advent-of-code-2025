import sys

def is_repetition_list(seq):
    n = len(seq)
    # i es el tamaño del bloque que selecciono
    for i in range(1, n // 2 + 1):
        # si no es divisible el numero por el bloque paso al siguiente
        if n % i != 0:
            continue
        veces_que_cabe = n // i
        patron = seq[:i]
        
        if patron * veces_que_cabe == seq:
            return True, patron
    return False, []
        

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