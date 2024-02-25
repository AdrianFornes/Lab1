import random

# Generar un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

# Inicializar contador de intentos
intentos = 0

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
