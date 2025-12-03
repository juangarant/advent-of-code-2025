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
                vueltas = 0
                paso = paso.replace(",", "").replace(".", "").strip()

                if not paso: continue

                letra = paso[0].upper()
                numero = int(paso[1:])

                
                #mal tengo que revisar los ceros intermedios, por ejemplo si tengo R200 mi codigo devuelve 2, pero tendría
                if letra == "R":
                    if ((numero+dial) %100) != 0: vueltas = (numero + dial) // 100
                    dial = (dial + numero) % 100

                elif letra == "L":
                    if ((numero-dial) %100) != 0: vueltas = (numero + dial) // 100
                    dial = (dial - numero) % 100
            
                if dial%100 == 0:
                    print(f"El acumulador volvió a cero con el paso: {paso}")
                    contador += 1
                contador += vueltas


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
                
    