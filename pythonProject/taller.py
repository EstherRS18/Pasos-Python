nombre = (input("Ingrese su nombre: "))
Salario = float(input("Ingrese su salario: "))
horas_extra = float(input("Ingrese las horas extra trabajadas: "))
horas_trabajadas = float(input("cuantas horas trabajo"))
salario_base =int(input("valor hora"))
valor_hora_extra = float(input("Ingrese el valor por hora extra: "))

salario_base_total = horas_trabajadas * salario_base
salario_extra = horas_extra * valor_hora_extra
salario_total = salario_base_total + salario_extra

# Imprimir colilla de pago
print("\nColilla de Pago")
print("Nombre: {}".format(nombre))
print("Horas Trabajadas: {}".format(horas_trabajadas))
print("Salario Base por Hora: ${}".format(salario_base))
print("Salario Base Total: ${}".format(salario_base_total))
print("Horas Extra: {}".format(horas_extra))
print("Valor Hora Extra: ${}".format(valor_hora_extra))
print("Salario por Horas Extra: ${}".format(salario_extra))
print("Salario Total: ${}".format(salario_total))