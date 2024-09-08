from typing import List, Tuple

# Leer el contenido de los archivos
def leer_archivo(nombre_archivo: str) -> str:
    """
    Lee el contenido de un archivo de texto y lo devuelve como una cadena

    Argumentos:
        nombre_archivo (str): El nombre del archivo que se va a leer

    Returns:
        str: El contenido del archivo como cadena de texto
    """
    with open(nombre_archivo, 'r') as file:
        return file.read()  # Leemos todo el contenido del archivo
    
# Función para calcular el array de "lps" que mantiene la longitud del prefijo más largo
def calcular_lps(pattern: str) -> List[int]:
    """
    Calcula el array 'lps' (longest prefix suffix) para un patrón dado

    Argumentos:
        pattern (str): El patrón del cual se calculará el array lps

    Returns:
        List[int]: Una lista que representa la longitud del prefijo más largo que también es sufijo
    """
    lps = [0] * len(pattern)  # Inicializamos el array lps con ceros
    length = 0  # Longitud del prefijo más largo previo
    i = 1  # Empezamos desde el segundo carácter (índice 1)

    # Iteramos sobre el patrón para calcular lps
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            # Si hay coincidencia entre el carácter actual y el prefijo más largo
            length += 1
            lps[i] = length
            i += 1
        else:
            # Si no coincide, reducimos la longitud del prefijo
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps  # Retornamos el array lps


# Función de KMP para verificar si un patrón está en el texto
def kmp_search(pattern: str, text: str) -> bool:
    """
    Implementa el algoritmo KMP para verificar si un patrón está contenido en un texto

    Argumentos:
        pattern (str): El patrón a buscar
        text (str): El texto en el que se busca el patrón

    Returns:
        bool: Retorna True si el patrón se encuentra en el texto, de lo contrario, False
    """
    if not pattern:  # Si el patrón es vacío, retornar True
        return True
    m = len(pattern)
    n = len(text)
    lps = calcular_lps(pattern)  # Calculamos el array lps del patrón
    i = 0  # Índice para el texto
    j = 0  # Índice para el patrón

    # Iteramos sobre el texto
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            # Si encontramos el patrón, retornamos True
            return True

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False  # Retornamos False si no encontramos el patrón



# Función para transformar el texto agregando un delimitador especial (#)
def preparar_texto(text: str) -> str:
    """
    Transforma un texto agregando un delimitador especial '#' para manejar palíndromos de longitud impar y par

    Argumentos:
        text (str): El texto original

    Returns:
        str: El texto modificado con delimitadores
    """
    # Agregamos '#' entre cada carácter para manejar palíndromos de longitud impar y par
    return '#' + '#'.join(text) + '#'


# Algoritmo de Manacher para encontrar el palíndromo más largo en un texto
def manacher(text: str) -> Tuple[int, int]:
    """
    Implementa el algoritmo de Manacher para encontrar el palíndromo más largo en un texto

    Argumentos:
        text (str): El texto en el cual se busca el palíndromo

    Returns:
        Tuple[int, int]: Las posiciones (inicial y final) del palíndromo más largo
    """
    if not text:  # Si el texto es vacío, retornar (1, 0)
        return 1, 0

    # Preparamos el texto para manejar tanto palíndromos pares como impares
    T = preparar_texto(text)
    n = len(T)  # Longitud del texto preparado
    P = [0] * n  # Array que guardará los radios de los palíndromos
    center = 0  # Centro del palíndromo más largo
    right = 0   # Borde derecho del palíndromo más largo

    # Iteramos sobre el texto preparado
    for i in range(n):
        mirror = 2 * center - i  # Calculamos la posición espejo respecto al centro

        if i < right:
            P[i] = min(right - i, P[mirror])  # Limitamos la expansión si estamos dentro del borde derecho

        # Intentamos expandir el palíndromo centrado en i
        while i + P[i] + 1 < n and i - P[i] - 1 >= 0 and T[i + P[i] + 1] == T[i - P[i] - 1]:
            P[i] += 1

        # Actualizamos el centro y el borde derecho si el palíndromo actual es más grande
        if i + P[i] > right:
            center = i
            right = i + P[i]

    # Encontrar el palíndromo más largo
    max_len = max(P)  # Longitud máxima del palindromo
    center_index = P.index(max_len)  # indice del centro del palíndromo más largo

    # Corregimos los índices de inicio y fin en el texto original
    inicio = (center_index - max_len) // 2
    fin = (center_index + max_len) // 2 - 1  # Ajustamos para corregir el indice final

    return inicio + 1, fin + 1  # Retornamos las posiciones en base 1


# Encuentra la subcadena común más larga entre dos cadenas
def longest_common_substring(s1: str, s2: str) -> Tuple[int, int]:
    """
    Encuentra y obtiene las posiciones (inicio y final) de la subcadena más larga que es 
    común entre dos cadenas de texto utilizando una tabla de programación dinámica. 
    Este método compara cada carácter de ambas cadenas para identificar la secuencia 
    continua más larga entre los archivos de transmisión.

    Argumentos:
        s1 (str): La primera cadena de texto
        s2 (str): La segunda cadena de texto

    Returns:
        Tuple[int, int]: Una tupla con las posiciones inicial y final (en base 1) 
        de la subcadena más larga encontrada en la primera cadena
    """
    # Creamos una tabla para almacenar las longitudes de las subcadenas comunes
    m = [[0] * (1 + len(s2)) for _ in range(1 + len(s1))]
    longest, x_longest = 0, 0  # Longitud de la subcadena más larga y su posición en s1

    # Iteramos sobre ambas cadenas para encontrar la subcadena común más larga
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1  # Incrementamos la longitud si hay coincidencia
                if m[x][y] > longest:
                    longest = m[x][y]  # Actualizamos la longitud más larga
                    x_longest = x  # Guardamos la posición en s1

    return x_longest - longest + 1, x_longest  # Retornamos las posiciones inicial y final


# Función principal para ejecutar el análisis completo
def ejecutar_analisis() -> None:
    """
    Ejecuta el análisis completo del programa que incluye todas las partes de las instrucciones:
    - Parte 1: Búsqueda de secuencias maliciosas en los archivos de transmisión
    - Parte 2: Identificación del palíndromo más largo en cada archivo de transmisión
    - Parte 3: Detección de la subcadena común más larga entre los archivos de transmisión

    Muestra los resultados de cada parte
    """
    # Archivos de transmisión y códigos maliciosos
    transmission_files = ['transmission1.txt', 'transmission2.txt']
    mcode_files = ['mcode1.txt', 'mcode2.txt', 'mcode3.txt']
    
    # Parte 1: Verificamos si el código malicioso está en los archivos de transmisión
    print("Parte 1: Búsqueda de secuencias maliciosas")
    resultados_parte1 = [
        (mcode_file, transmission_file, kmp_search(leer_archivo(mcode_file), leer_archivo(transmission_file)))
        for mcode_file in mcode_files
        for transmission_file in transmission_files
    ]
    for mcode_file, transmission_file, resultado in resultados_parte1:
        print(f"'{mcode_file}' está contenido en '{transmission_file}': {resultado}")

    # Parte 2: Buscamos el palíndromo más largo en cada archivo de transmisión
    print("\nParte 2: Palíndromo más largo")
    resultados_parte2 = [
        (transmission_file, manacher(leer_archivo(transmission_file)))
        for transmission_file in transmission_files
    ]
    for transmission_file, (inicio, fin) in resultados_parte2:
        print(f"El palíndromo más largo en '{transmission_file}' está entre las posiciones {inicio} y {fin}")

    # Parte 3: Buscamos la subcadena común más larga entre los dos archivos de transmisión
    print("\nParte 3: Subcadena común más larga entre archivos de transmisión")
    contenido_transmision1 = leer_archivo('transmission1.txt')
    contenido_transmision2 = leer_archivo('transmission2.txt')
    inicio, fin = longest_common_substring(contenido_transmision1, contenido_transmision2)
    print(f"Posición inicial y final del substring más largo común en el archivo de transmisión 1: {inicio} {fin}")


if __name__ == "__main__":
    ejecutar_analisis()
