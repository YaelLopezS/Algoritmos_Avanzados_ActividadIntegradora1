# Importar las funciones necesarias
from kmp import leer_archivo, kmp_search
from manacher import manacher
from typing import Tuple

def longest_common_substring(s1: str, s2: str) -> Tuple[int, int]:
    """
        Encuentra la subcadena más larga que es común entre dos cadenas de texto 
        utilizando una tabla de programación dinámica. Este método compara cada 
        carácter de ambas cadenas para identificar la secuencia continua más larga.

        Args:
        s1 (str): La primera cadena de texto.
        s2 (str): La segunda cadena de texto.

        Returns:
        Tuple[int, int]: Una tupla con las posiciones inicial y final (en base 1) 
        de la subcadena más larga encontrada en la primera cadena.
    """
    m = [[0] * (1 + len(s2)) for _ in range(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x

    return x_longest - longest + 1, x_longest

def ejecutar_analisis():
    """
    Ejecuta el análisis completo del programa, que incluye:
    - Parte 1: Búsqueda de secuencias maliciosas en los archivos de transmisión.
    - Parte 2: Identificación del palíndromo más largo en cada archivo de transmisión.
    - Parte 3: Detección de la subcadena común más larga entre los archivos de transmisión.

    Muestra los resultados de cada parte del análisis en un formato organizado.
    """
    # Archivos a analizar
    transmission_files = ['transmission1.txt', 'transmission2.txt']
    mcode_files = ['mcode1.txt', 'mcode2.txt', 'mcode3.txt']
    
    # Parte 1: Verificar si el código malicioso está contenido en los archivos de transmisión
    print("Parte 1: Búsqueda de secuencias maliciosas")
    resultados_parte1 = [
        (mcode_file, transmission_file, kmp_search(leer_archivo(mcode_file), leer_archivo(transmission_file)))
        for mcode_file in mcode_files
        for transmission_file in transmission_files
    ]
    for mcode_file, transmission_file, resultado in resultados_parte1:
        print(f"'{mcode_file}' está contenido en '{transmission_file}': {resultado}")

    # Parte 2: Encontrar el palíndromo más largo en cada archivo de transmisión usando Manacher
    print("\nParte 2: Palíndromo más largo")
    resultados_parte2 = [
        (transmission_file, manacher(leer_archivo(transmission_file)))
        for transmission_file in transmission_files
    ]
    for transmission_file, (inicio, fin) in resultados_parte2:
        print(f"El palíndromo más largo en '{transmission_file}' está entre las posiciones {inicio} y {fin}")

    # Parte 3: Encontrar la subcadena común más larga entre los dos archivos de transmisión
    print("\nParte 3: Subcadena común más larga entre archivos de transmisión")
    contenido_transmision1 = leer_archivo('transmission1.txt')
    contenido_transmision2 = leer_archivo('transmission2.txt')
    inicio, fin = longest_common_substring(contenido_transmision1, contenido_transmision2)
    print(f"Posición inicial y final del substring más largo común en el archivo de transmisión 1: {inicio} {fin}")

# Ejecutar la función principal
if __name__ == "__main__":
    ejecutar_analisis()
