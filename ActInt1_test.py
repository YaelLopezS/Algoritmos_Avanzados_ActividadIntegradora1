import pytest
from ActInt1 import kmp_search, manacher, longest_common_substring

# Pruebas para KMP (Knuth-Morris-Pratt)

def test_kmp_search_basic():
    assert kmp_search("abc", "abcabc") == True
    assert kmp_search("xyz", "abcabc") == False

def test_kmp_search_empty_pattern():
    # Patrón vacío debe devolver True
    assert kmp_search("", "abcabc") == True
    # Patrón y texto vacíos deben devolver True
    assert kmp_search("", "") == True

def test_kmp_search_empty_text():
    # Texto vacío con patrón no vacío debe devolver False
    assert kmp_search("abc", "") == False

def test_kmp_search_pattern_longer_than_text():
    # Patrón más largo que el texto debe devolver False
    assert kmp_search("abcdef", "abc") == False

def test_kmp_search_repeated_pattern():
    # Patrón repetido varias veces en el texto
    assert kmp_search("abc", "abcabcabc") == True



# Pruebas para el algoritmo de Manacher

def test_manacher_single_char():
    # Un solo carácter es un palíndromo por sí solo
    assert manacher("a") == (1, 1)

def test_manacher_no_palindrome():
    # No hay palíndromo significativo
    assert manacher("abc") == (1, 1)

def test_manacher_full_palindrome():
    # Texto completamente palindrómico
    assert manacher("racecar") == (1, 7)

def test_manacher_multiple_palindromes_same_length():
    # Hay varios palíndromos de la misma longitud
    assert manacher("abccba") == (1, 6)

def test_manacher_empty_string():
    # Texto vacío
    assert manacher("") == (1, 0)

def test_manacher_palindrome_at_start():
    # El palíndromo más largo está al principio
    assert manacher("abcba12345") == (1, 5)



# Pruebas para la subcadena común más larga

def test_longest_common_substring_no_common():
    # Sin subcadena común
    assert longest_common_substring("abc", "def") == (1, 0)

def test_longest_common_substring_one_char():
    # Una sola letra en común
    assert longest_common_substring("abc", "b") == (2, 2)

def test_longest_common_substring_identical_strings():
    # Cadenas idénticas
    assert longest_common_substring("abcde", "abcde") == (1, 5)

def test_longest_common_substring_empty_string():
    # Una cadena vacía
    assert longest_common_substring("abcde", "") == (1, 0)
    assert longest_common_substring("", "abcde") == (1, 0)

def test_longest_common_substring_common_suffix():
    # Sufijo común
    assert longest_common_substring("abcdef", "def") == (4, 6)

def test_longest_common_substring_large_strings_small_common():
    # Cadenas largas con una subcadena común pequeña
    assert longest_common_substring("abcdefghij", "zabcfxyz") == (1, 3)

if __name__ == "__main__":
    pytest.main()
