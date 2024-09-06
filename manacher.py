# Importamos las funciones KMP del archivo kmp.py
from kmp import leer_archivo, kmp_search

# Función para transformar el texto agregando un delimitador especial (#)
def preparar_texto(text):
    return '#' + '#'.join(text) + '#'

# Algoritmo de Manacher para encontrar el palíndromo más largo en un texto
def manacher(text):
    # Preparar el texto con delimitadores
    T = preparar_texto(text)
    n = len(T)
    P = [0] * n  # Array que guardará el radio de los palíndromos
    center = 0  # Centro del palíndromo más grande encontrado
    right = 0   # Borde derecho del palíndromo más grande encontrado
    
    for i in range(n):
        mirror = 2 * center - i  # Posición espejo respecto al centro

        if i < right:
            P[i] = min(right - i, P[mirror])

        # Intentar expandir el palíndromo centrado en i
        while i + P[i] + 1 < n and i - P[i] - 1 >= 0 and T[i + P[i] + 1] == T[i - P[i] - 1]:
            P[i] += 1

        # Actualizar centro y borde derecho si encontramos un palíndromo más grande
        if i + P[i] > right:
            center = i
            right = i + P[i]

    # Encontrar el tamaño del palíndromo más grande
    max_len = max(P)
    center_index = P.index(max_len)
    
    # Convertir la posición en el texto modificado al texto original
    inicio = (center_index - max_len) // 2
    fin = (center_index + max_len) // 2
    
    return inicio + 1, fin + 1  # Retornar posiciones en base 1

# Archivos a analizar
transmission_files = ['transmission1.txt', 'transmission2.txt']
mcode_files = ['mcode1.txt', 'mcode2.txt', 'mcode3.txt']


# Encontrar el palíndromo más largo en cada archivo de transmisión usando Manacher
for transmission_file in transmission_files:
    transmission_content = leer_archivo(transmission_file)
    inicio, fin = manacher(transmission_content)
    print(f"El palíndromo más largo en '{transmission_file}' está entre las posiciones {inicio} y {fin}")
