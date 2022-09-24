# Reto #3
# ¿ES UN NÚMERO PRIMO?
# Dificultad: MEDIA

# Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.

def isPrimeNumber(number):
    if (number < 2): 
        return False

    for n in range(2, number):
        if (number % n == 0):
            return False
    
    return True

for n in range(1, 100):
    if (isPrimeNumber(n)):
        print(n)