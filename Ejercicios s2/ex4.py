import random

# Crear una lista de 10 números aleatorios
numeros = [random.randint(1, 100) for _ in range(10)]

# Inicializar variables para el promedio de los números pares y el producto de los números impares
suma_pares = 0
contador_pares = 0
producto_impares = 1

# Iterar sobre la lista de números
for num in numeros:
    if num % 2 == 0:  # Si el número es par
        suma_pares += num
        contador_pares += 1
    else:  # Si el número es impar
        producto_impares *= num

# Calcular el promedio de los números pares
if contador_pares != 0:
    promedio_pares = suma_pares / contador_pares
else:
    promedio_pares = 0

# Imprimir resultados
print(f"Lista de números: {numeros}")
print(f"Promedio de números pares: {promedio_pares}")
print(f"Producto de números impares: {producto_impares}")

