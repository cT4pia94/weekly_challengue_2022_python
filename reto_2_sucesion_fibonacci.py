
# Reto #2
# LA SUCESIÓN DE FIBONACCI
# Dificultad: DIFÍCIL

# Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
# La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13...

valor_base = 0
valor_extra = 1
total = 0

for i in range(0, 50):
    
    print(valor_base)

    total = valor_base + valor_extra
    valor_base = valor_extra
    valor_extra = total


