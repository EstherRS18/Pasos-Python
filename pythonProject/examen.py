#Rodelo Saenz Yeidy Esther

nombre = (input("Ingrese su nombre: "))
num_hijos = int(input("Ingrese el número de hijos: "))
valor_hora = float(input("Ingrese el valor de la hora de trabajo: "))
horas_trabajadas = float(input("Dijite las horas trabajadas en la semana: "))

if num_hijos > 3:
    boni_hijos = 10 * num_hijos
else:
    boni_hijos = 5 * num_hijos

if horas_trabajadas > 47:
    horas_extras = horas_trabajadas - 47
else:
    horas_extras = 0

valor_horas_semana = 47 * valor_hora


valor_extras = 0
if horas_extras > 0:
    valor_extras = horas_extras * valor_hora * 1.35


devengado_horas_extras = valor_horas_semana + valor_extras
neto_a_pagar = devengado_horas_extras + boni_hijos

print("\nResumen de salario:")
print(f"Nombre del empleado: {nombre}")
print(f"Número de hijos: {num_hijos}")
print(f"Bonificación por hijos: {boni_hijos} horas")
print(f"Valor de la hora de trabajo: ${valor_hora:.2f}")
print(f"Horas trabajadas en la semana: {horas_trabajadas} horas")
print(f"Valor de horas (47 horas semana): ${valor_horas_semana:.2f}")
print(f"Horas extras: {horas_extras} horas")
print(f"Valor de extras: ${valor_extras:.2f}")
print(f"Devengado por horas extras + las 47: ${devengado_horas_extras:.2f}")
print(f"Neto a pagar (con bonificación de hijos): ${neto_a_pagar:.2f}")
