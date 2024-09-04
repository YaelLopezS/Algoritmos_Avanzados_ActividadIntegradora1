# Función para calcular el array de "lps" que mantiene la longitud del prefijo más largo
def calcular_lps(pattern):
    lps = [0] * len(pattern)
    length = 0  # Longitud del prefijo más largo previo
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

# Función de KMP para verificar si un patrón está en el texto
def kmp_search(pattern, text):
    m = len(pattern)
    n = len(text)
    lps = calcular_lps(pattern)
    i = 0  # Índice para text[]
    j = 0  # Índice para pattern[]

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            return True  # Aquí se retorna True, indicando que se encontró el patrón

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return False

# Leer el contenido de los archivos
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as file:
        return file.read()

# Archivos a analizar
transmission_files = ['transmission1.txt', 'transmission2.txt']
mcode_files = ['mcode1.txt', 'mcode2.txt', 'mcode3.txt']

# Comparar el contenido de cada mcode con cada transmission
for mcode_file in mcode_files:
    mcode_content = leer_archivo(mcode_file)
    for transmission_file in transmission_files:
        transmission_content = leer_archivo(transmission_file)
        resultado = kmp_search(mcode_content, transmission_content)
        print(f"'{mcode_file}' está contenido en '{transmission_file}': {resultado}")