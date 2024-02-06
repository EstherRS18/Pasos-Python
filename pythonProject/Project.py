import random

departamentos = {}

departamentos = {
 "Antioquia" : "Medellin",
 "Atlántico": "Barranquilla",
 "Caldas": "Manizales",
 "Chocó": "Quibdó",
 "Córdoba": "Montería",
 "Nariño": "Pasto",
 "Tolima": "Ibagué",
 "Valle del Cauca": "Cali",
}

print("Diccionario de Departamentos:")
for departamento, _ in departamentos.items():
    print(f"{departamento}")

departamento_azar = random.choice(list(departamentos.keys()))
capital_correcta = departamentos[departamento_azar]


