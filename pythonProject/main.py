import random

Departamentos = {}

Departamentos = {
    "Antioquia": "Medellin",
    "Atlántico": "Barranquilla",
    "Caldas": "Manizales",
    "Chocó": "Quibdó",
    "Córdoba": "Montería"
}

print("Diccionario de Departamentos:")
for departamento, _ in Departamentos.items():
    print(f"{departamento}")

departamento_azar = random.choice(list(Departamentos.keys()))
capital_correcta = Departamentos[departamento_azar]

intentos = 3
for _ in range(intentos):
    respuesta_usuario = input(f"Ingrese la capital de {departamento_azar}: ").capitalize()


    if respuesta_usuario == capital_correcta:
        print("¡Correcto!")
        break
    elif respuesta_usuario.lower() == 'salir':
        print("Hasta luego.")
        break

    else:
        print(f"Incorrecto. Te quedan {intentos - 1} intentos.")
        intentos -= 1
else:
    print("Hasta luego. Has agotado tus intentos.")

