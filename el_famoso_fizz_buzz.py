# Reto #0
# EL FAMOSO "FIZZ BUZZ"
# Fecha publicación enunciado: 27/12/21
# Fecha publicación resolución: 03/01/22
# Dificultad: FÁCIL
# Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

for i in range(1, 100):
    if (i % 3 == 0 and i % 5 == 0):
        print('fizz buzz')

    elif (i % 5 == 0):
        print('buzz')

    elif (i % 3 == 0):
        print('fizz')

    else:
        print(i)