import sys

def procesar_texto(texto_entrada):
    dial = 50
    contador = 0

    try:
        with open(texto_entrada, 'r', encoding='utf-8') as archivo:
            #.read lee todo el archivo como un solo string
            texto_entrada = archivo.read()
            #uso split para separar cortar el texto por espacios, saltos de línea, tabulaciones (en este caso saltos de línea)
            lista = texto_entrada.split()

            for paso in lista:
                paso = paso.replace(",", "").replace(".", "").strip()

                if not paso: continue

                letra = paso[0].upper()
                numero = int(paso[1:])

                if letra == "R":
                    # Girar a la derecha: de dial a (dial + numero)
                    # Contamos cuántas veces pasamos por 0
                    # Si dial=50 y numero=60, vamos de 50 a 110, pasamos por 100 (que es 0)
                    veces_por_cero = (dial + numero) // 100
                    dial = (dial + numero) % 100
                    
                elif letra == "L":
                    # Girar a la izquierda: de dial a (dial - numero)
                    # Si dial=50 y numero=68, vamos de 50 hacia abajo 68 clicks
                    # Pasamos por 0 cuando dial - clicks = 0, es decir cuando clicks = dial
                    # Entonces pasamos por 0 cada 100 clicks después del primer 0
                    # Número de veces que pasamos por 0 = (numero + (100 - dial)) // 100
                    if dial == 0 and numero % 100 == 0:
                        veces_por_cero = (numero // 100)
                    elif numero > dial:
                        veces_por_cero = 1 + (numero - dial) // 100
                    else:
                        veces_por_cero = 0
                    dial = (dial - numero) % 100
                
                print(f"Paso: {paso}, Dial ahora: {dial}, Veces por cero: {veces_por_cero}")
                contador += veces_por_cero

        return contador
    except FileNotFoundError:
        print(f"Error: El archivo '{texto_entrada}' no se encontró.")
        return None
    except ValueError:
        print("Error: El archivo contiene datos no válidos.")
        return None
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python secret-entrance.py <ruta_del_archivo>")
        sys.exit(1)

    ruta_archivo = sys.argv[1]
    resultado = procesar_texto(ruta_archivo)

    if resultado is not None:
        print(f"Número de veces que el acumulador vuelve a cero: {resultado}")
                
    