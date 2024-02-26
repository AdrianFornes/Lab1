# Lab1
##  Reporte parctica 1 de LRT4102

### RESUMEN 

Para esta practica de laboratoria se dio una introduccion hacia lo que es ubuntu, python y Ros. En el cual se adquirirron nuevos conocimientos como la instalacion de una maquina viertual, programacion basica de python y la instalacion de softwarer ROS. 

### INTRODUCCION

Python, un lenguaje de programación de alto nivel, se ha vuelto muy popular gracias a su facilidad de uso y versatilidad. Python se ha convertido en una opción ideal para cualquier programador porque es fácil de aprender y de leer. Abarca una amplia gama de aplicaciones, desde el desarrollo web hasta el análisis de datos y el aprendizaje automático, gracias a su sintaxis clara y estructurada.

Python se destaca por su amplia gama de escenarios. Lo convierte en una herramienta útil para cualquier programador debido a su capacidad para adaptarse an una variedad de dominios, como el desarrollo de software, el scripting y la automatización. Cuenta con una amplia biblioteca estándar que facilita tareas comunes gracias a su enfoque de "baterías incluidas".

Algunas de sus principales beneficiios es la sintaxis limpia y fácil de leer de Python ya que facilita la escritura de código y mejora la colaboración entre varias personas. APor otra parte, su naturaleza interpretada permite una rápida iteración y desarrollo al eliminar la necesidad de un paso de compilación. La abundante documentación y la comunidad activa de Python son recursos valiosos para resolver problemas y mejorar habilidades.

Como todo lenguaje de programacion tiene tipos de variables, Python es tipado dinámicamente, por lo que no es necesario declarar el tipo de una variable al asignarle un valor. Los enteros, los números de punto flotante, las cadenas de texto, las listas y los diccionarios son algunos de los tipos de variables comunes. Esta flexibilidad facilita la manipulación de estructuras y datos.

Otros comandos de Python tienen funciones que simplifican tareas comunes, como la manipulación de listas (append(), remove()), la gestión de cadenas (split(), join()), y la entrada/salida de datos (input(), print()).

Python se destaca como un lenguaje poderoso y versátil para abordar desafíos complejos en el desarrollo de software y más allá, además de ser fácil de usar para principiantes. Su amplio conjunto de herramientas, sintaxis clara y comunidad activa lo convierten en un favorito en el mundo de la programación.

Operaciones con int (Enteros):

* Suma (+): Se utiliza para sumar dos números enteros.
* Resta (-): Resta el segundo número entero del primero.
* Multiplicación (*): Multiplica dos números enteros.
* División (/): Divide el primer número entero por el segundo, devolviendo un resultado de punto flotante incluso si la división es exacta.
* División entera (//): Devuelve la parte entera de la división, descartando el residuo.
* Módulo (%): Devuelve el residuo de la división entera entre dos números enteros.
* Potencia ():** Eleva el primer número entero a la potencia del segundo.

Operaciones con str (Cadenas de texto):

* Concatenación (+): Une dos cadenas de texto.
* Repetición (*): Repite una cadena de texto por un número específico de veces.
*  Indexación ([]): Permite acceder a caracteres específicos dentro de una cadena mediante su posición.
* Slicing ([:]): Extrae una porción de una cadena, especificando el rango de índices.
* Longitud (len()): Devuelve la cantidad de caracteres en una cadena.

Operaciones con float (Punto flotante):

* Las operaciones con float son similares a las de int e incluyen suma, resta, multiplicación, división y potenciación.

Operaciones con bool (Booleanos):

* Operadores lógicos (and, or, not): Permiten realizar operaciones lógicas entre dos booleanos (y, o, no).
* Comparadores (<, <=, >, >=, ==, !=): Se utilizan para comparar dos valores y devolver un booleano según la relación (menor que, menor o igual, mayor que, mayor o igual, igual, no igual).
* Conversión (bool()): Puede convertir otros tipos de datos a booleanos.

Operaciones con complex (Números complejos):

* Creación (complex(real, imag)): Permite crear números complejos especificando sus partes real e imaginaria.
* Conjugado (conjugate()): Devuelve el conjugado de un número complejo.
* Suma, resta, multiplicación y división: Se realizan de manera similar a los números reales, teniendo en cuenta las partes real e imaginaria.

### PROBLEMAS 

1.  Escribir un programa que lea un entero positivo “n” introducido por el usuario y después muestre
en pantalla la suma de todos los enteros desde 1 hasta n . La suma de los primeros enteros
positivos puede ser calculada de la siguiente forma:


    $ suma =\frac{n(n+1)}{2}$

2. Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo por hora.
Después debe mostrar por pantalla la paga que le corresponde.

3. Crea una lista de nombre + sueldo por hora + horas trabajadas de al menos seis operadores.
Imprime el nombre y el sueldo a pagar de cada operador.

4. Problema 4 
* Crea una lista llamada numeros que contenga al menos 10 números.
* Calcula el promedio de los números pares y el producto de los números impares.
* Imprime los resultados.

5. Crea un programa que solicite al usuario adivinar un número secreto. El programa debe generar
un número aleatorio entre 1 y 10, y el usuario debe intentar adivinarlo. El programa debe
proporcionar pistas si el número ingresado por el usuario es demasiado alto o bajo. El bucle while
debe continuar hasta que el usuario adivine correctamente. Al final se debe imprimir en cuantos
intentos el usuario logró adivinar el número.

6. Robot explorador
* El programa debe generar una matriz de al menos 5x5.
* El robot inicia su camino en la posición (0,0) de la matriz y debe salir en la posición (4,4) o la
máxima posición si se cambia el tamaño de matriz.
* El numero y la posición de los obstáculos es aleatoria.
* El robot solo puede avanzar, girar a la izquierda o a la derecha para buscar un camino libre, en el
eventual caso que el robot no pueda salir debe imprimir en pantalla “Imposible llegar al destino”
* En caso de que el robot llegue a su destino final deberá imprimir el mapa, con los espacios libres y
obstáculos de la siguiente forma X obstáculo o libre
* Deberá imprimir también la ruta que siguió.
* Mostrar un segundo mapa con el “camino” seguido por el robot mediante flechas 

### Soluciones 

1. Para este problema se realizo un codigo en el cual se obtien un numero entero dada por el usuario y se have la suma hasta el numero que se introdujo en la terminal, dando como resultado la sume de los enteros hasta el numero "n". 

```adrian
# declarar varibale para un numero entero 
n = int(input("Introduce un número entero: "))
# Se realiza la operaciohoras = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
paga = horas * coste
print("Tu paga es", paga)   

```

Primero se le pidio al usuario que agregara una variabnle en este caso int parqa el numnero entero, despues se introdijo la formula requerida opara hacer la suma d elos enteros y hatsa el final conn un print se imprimio el resulrtaso que da la suma de la ecuacion dada en el codigo.

2. Para el segundo problema se realizo un codigo donde se le pregunta al usuario el numero de horas trabajadas y el costo de cada una de las horas, esto se logro con el siguiente codigo:


```adrian
#se indica una variable float para las horas
horas = float(input("Introduce tus horas de trabajo: "))
#otra variable float para el costo 
coste = float(input("Introduce lo que cobras por hora: "))
#oipewracion para saber el salario 
paga = horas * coste
# se imprime la paga 
print("Tu paga es", paga)

```

Como se observa en el codigo anterior se puso una variable float para las horas trabajadas, de ahi se le pide al usuario que intriodusca el costo tambien con una variable float al final se calcula mediante una operacion multiplicadora las horas por la paga y se obtiene el resultado, finalmente se imprime el resultado de la operacion obteniendo cuanto se le va a pagar dependiendo de las horas trabajadas.

3. Para el tercer ejercicio se relaizo un codigo que genere una lista de trabajadores, obteniendo su paga mediante las horas trabajdas y el costo de cada hora. 

```adrian

# Crear un diccionario con la información de los operadores
operadores = {
    'Lalo': {'sueldo_por_hora': 10, 'horas_trabajadas': 40},
    'Juan': {'sueldo_por_hora': 12, 'horas_trabajadas': 35},
    'Alain': {'sueldo_por_hora': 15, 'horas_trabajadas': 30},
    'Pedro': {'sueldo_por_hora': 8, 'horas_trabajadas': 45},
    'Jesus': {'sueldo_por_hora': 20, 'horas_trabajadas': 25},
    'Adrian': {'sueldo_por_hora': 18, 'horas_trabajadas': 38},
}

# Imprimir nombre y sueldo de cada operador
for operador, info in operadores.items():
    nombre = operador
    sueldo_por_hora = info['sueldo_por_hora']
    horas_trabajadas = info['horas_trabajadas']
    sueldo_a_pagar = sueldo_por_hora * horas_trabajadas

    print(f'Operador: {nombre}, Sueldo a pagar: ${sueldo_a_pagar}')


```

Para este codigo que se muestra anteriormente primero se genera una lista de trabajadopres con nombre, suledo por hora y las horas trabajadas, subsecuente a la lista se realiza la operacion de cuanto se va  pagr a cada trabajador dependiendo de la lis, imprimoierntop su nombre y su sueldo.

4. Para el cuerto problema se realizo un codigo en el cual se generar 10 numeros enteros al azar, despues se analiza los pares y los impares, a los impares se les sacara el producto de ellos obteniendo elk resultado.

```adrian

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


```

Para este codigo se generaron 10 numeros aleatorios con "random.randint", teniendo un rango de 1 a 10 para solo obtener 10 numeros. 

Subsecuente a eso se obtuvieron los numeros impares de esos 10 numeros generados, generando la operacion para el producto de los impares, obteniendo el resultado final , 9imprimiendo los numeros impares y el producto de los mismos.

5. Para el quinto problema se realizo un codigo en el cual es u juego de adivinar el numero generado, dando pistas si estas cerca o ya pusiste de mas.

```adrian

import random

# Generar un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

# Inicializar contador de intentos
intentos = 0
horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
paga = horas * coste
print("Tu paga es", paga)
print("¿Que numero esto pensando entre 1 y 10?")

while True:
    # Solicitar al usuario que ingrese un número
    intento_usuario = int(input("Adivina :): "))
    
    # Incrementar el contador de intentos
    intentos += 1
    
    # Verificar si el número ingresado es correcto
    if intento_usuario == numero_secreto:
        print(f"¡Lo adivinaste en {intentos} intentos!")
        break
    else:
        # Proporcionar pistas
        if intento_usuario > numero_secreto:
            print("Te pasaste.")
        else:
            print("Te falta.")
```

En el codigo anterior se muestra como se genera un numero aleatorio entre 1 y 10 con la variable "random.randint", por otro lado se hizo una comparacion en la cual se indica que si el numero introducido por el usuaria es mayor al que fue generado se imprime un mensaje que dice "te passte", por otro lado si es menor a el bnumero generado imprime un mensaje que muestra "te falta", por otro lado si adivinas el numero se imprime un mensaje de los intentos en lo que lo lograste.

6. ERn el ultimo ejercicio se realizo un codigo el cual se hace un robot explarador que hace un camino para llegar al punto final.

```adrian
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

```

Para este codigo la primera parte es generar una matriz 5x5 agregando 5 filas y 5 columnas, siguente a esto se estipulan los espacios libres y los obsataculos que hay en la matriz, tosdo esto con numeros aleatoris que tienen el valor de "X" y los espacios libres "O".

Por otra parte se imprime la matriz ya con obstaculos y sus espacios libres, despues se pone el robot en la posicion inical que es (0,0) en la matriz, se utiliza un bucle while para simular el movimiento del robot hasta que llegue a la posición final.

Se utilizan condiciones para verificar si el robot puede moverse en una dirección específica sin chocar con obstáculos, al final se  imprime la matriz final con obstáculos y la ruta seguida por el robot en forma de flechas.

Si el robot no llega a la posicion final se imprime un mensaje "Imposible llegar al destino".

Este código simula de manera visual el movimiento de un robot en un entorno con obstáculos y proporciona información sobre el mapa resultante y la ruta tomada por el robot.

### CONCLUSION 

Al final de esta practica de laboratorio se obtuvo conocimiento basico de la programacion en python, como es su estructura y como funcionan las variables y las operaciones simples en este lenguaj, por otra parte la practica misma al realizar los 6 problemas requeridos en el laboratorio para poder reforzar los conocimientsos obtenidos que al final nos ayudaron a tener codigos entendibles y con resultados exitosos en el reporte.

Tambien, el conocuimiento basico de ROS y algunos comandos basicos para poder vincualr nuestra computadora virtual y GITHUB para poder trabajar simultaneamente, obteniendo un conocimiento basico para la utilizacion de los programas correctamente para poder trabajar de manera eficiente.



