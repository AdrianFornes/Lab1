import random

# Tamaño de la matriz
filas = 5
columnas = 5

# Inicializar matriz con espacios libres
matriz = [['o' for _ in range(columnas)] for _ in range(filas)]

# Agregar obstáculos de manera aleatoria
num_obstaculos = random.randint(5, 10)
for _ in range(num_obstaculos):
    fila_obstaculo = random.randint(0, filas - 1)
    columna_obstaculo = random.randint(0, columnas - 1)
    matriz[fila_obstaculo][columna_obstaculo] = 'X'

# Función para imprimir la matriz
def imprimir_matriz():
    for fila in matriz:
        print(' '.join(map(str, fila)))

# Inicializar posición del robot
posicion_actual = [0, 0]

# Inicializar dirección del robot
direccion = 'derecha'

# Inicializar ruta seguida por el robot
ruta = []

# Mientras el robot no esté en la posición final
while posicion_actual != [filas - 1, columnas - 1]:
    ruta.append(tuple(posicion_actual))
    # Determinar siguiente posición y dirección del robot
    if direccion == 'derecha':
        if posicion_actual[1] < columnas - 1 and matriz[posicion_actual[0]][posicion_actual[1] + 1] != 'X':
            posicion_actual[1] += 1
        elif posicion_actual[0] < filas - 1 and matriz[posicion_actual[0] + 1][posicion_actual[1]] != 'X':
            direccion = 'abajo'
        else:
            print("Imposible llegar al destino.")
            break
    elif direccion == 'abajo':
        if posicion_actual[0] < filas - 1 and matriz[posicion_actual[0] + 1][posicion_actual[1]] != 'X':
            posicion_actual[0] += 1
        elif posicion_actual[1] > 0 and matriz[posicion_actual[0]][posicion_actual[1] - 1] != 'X':
            direccion = 'izquierda'
        else:
            print("Imposible llegar al destino.")
            break
    elif direccion == 'izquierda':
        if posicion_actual[1] > 0 and matriz[posicion_actual[0]][posicion_actual[1] - 1] != 'X':
            posicion_actual[1] -= 1
        elif posicion_actual[0] > 0 and matriz[posicion_actual[0] - 1][posicion_actual[1]] != 'X':
            direccion = 'arriba'
        else:
            print("Imposible llegar al destino.")
            break
    elif direccion == 'arriba':
        if posicion_actual[0] > 0 and matriz[posicion_actual[0] - 1][posicion_actual[1]] != 'X':
            posicion_actual[0] -= 1
        elif posicion_actual[1] < columnas - 1 and matriz[posicion_actual[0]][posicion_actual[1] + 1] != 'X':
            direccion = 'derecha'
        else:
            print("Imposible llegar al destino.")
            break

# Imprimir resultado
if posicion_actual == [filas - 1, columnas - 1]:
    print("Mapa con espacios libres y obstáculos:")
    imprimir_matriz()
    print("\nRuta seguida por el robot:")
    for i in range(len(ruta)):
        if i < len(ruta) - 1:
            if ruta[i][0] < ruta[i + 1][0]:
                print("↓ ", end='')
            elif ruta[i][0] > ruta[i + 1][0]:
                print("↑ ", end='')
            elif ruta[i][1] < ruta[i + 1][1]:
                print("→ ", end='')
            elif ruta[i][1] > ruta[i + 1][1]:
                print("← ", end='')
        else:
            print("✓")

