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
