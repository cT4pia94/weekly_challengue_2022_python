
# Reto #1
# ¿ES UN ANAGRAMA?
# Fecha publicación enunciado: 03/01/22
# Fecha publicación resolución: 10/01/22
# Dificultad: MEDIA

# Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
# Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
# NO hace falta comprobar que ambas palabras existan.
# Dos palabras exactamente iguales no son anagrama.


def isAnagram(in1, in2):
    list1 = []
    list2 = []

    list1.extend(in1)
    list2.extend(in2)

    if in1 is None or in2 is None or len(in1) != len(in2):
        return False
    
    if len(in1) == len(in2):
        for a in list1:
            if a not in list2:
                return False

    return True

print(isAnagram('amor', 'roma'))  