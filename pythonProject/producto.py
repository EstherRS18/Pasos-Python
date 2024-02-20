# 1. Definición de variables
pasaje_adulto_guajira = 1450000
pasaje_adulto_canon_chicamocha = 1600000
pasaje_adulto_llanos_orientales = 1200000

pasaje_nino_guajira = 870000
pasaje_nino_canon_chicamocha = 960000
pasaje_nino_llanos_orientales = 720000

total_dinero_guajira = 0
total_dinero_canon_chicamocha = 0
total_dinero_llanos_orientales = 0

cantidad_personas_guajira = 0
cantidad_personas_canon_chicamocha = 0
cantidad_personas_llanos_orientales = 0

total_adultos = 0
total_ninos = 0
total_dinero = 0

# 2. Ciclo para ingresar datos de 10 clientes
clientes = [None] * 10
destino = [0] * 10
nro_adultos = [0] * 10
nro_ninos = [0] * 10
subtotales = [0] * 10
lugar_destino = None

for i in range(3):
    # Ingreso de datos para cada cliente
    clientes[i] = input("Por favor ingrese su nombre para registrar su viaje: ")
    destino[i] = int(input("Digite el numero de su destino: 1. Guajira, 2. Cañon del Chicamocha, 3.Llanos orientales: "))
    nro_adultos[i] = int(input("Digite cuantos adultos van: "))
    nro_ninos[i] = int(input("Digite cuantos niños van: "))

    if destino[i] == 1:
        subtotales[i] = (nro_adultos[i] * pasaje_adulto_guajira) + (nro_ninos[i] * pasaje_nino_guajira)
        lugar_destino = "Guajira"
        cantidad_personas_guajira += nro_adultos[i] + nro_ninos[i]
        total_dinero_guajira += subtotales[i]
    elif destino[i] == 2:
        subtotales[i] = (nro_adultos[i] * pasaje_adulto_canon_chicamocha) + (nro_ninos[i] * pasaje_nino_canon_chicamocha)
        lugar_destino = "Cañon Chicamocha"
        cantidad_personas_canon_chicamocha += nro_adultos[i] + nro_ninos[i]
        total_dinero_canon_chicamocha += subtotales[i]
    else:
        subtotales[i] = (nro_adultos[i] * pasaje_adulto_llanos_orientales) + (nro_ninos[i] * pasaje_nino_llanos_orientales)
        lugar_destino = "Llanos Orientales"
        cantidad_personas_llanos_orientales += nro_adultos[i] + nro_ninos[i]
        total_dinero_llanos_orientales += subtotales[i]

    # Imprimir cotización para cada cliente
    print("COTIZACION CLIENTE")
    print("nombre cliente:", clientes[i])
    print("lugar destino:", lugar_destino)
    print("numero adultos:", nro_adultos[i])
    print("numero niños:", nro_ninos[i])
    print("total:", subtotales[i])

    # Actualizar totales
    total_adultos += nro_adultos[i]
    total_ninos += nro_ninos[i]
    total_dinero += subtotales[i]

# Imprimir resultados totales
print("------------------------------------------------")
print("RESULTADOS TOTALES")
print("cantidad Personas Guajira:", cantidad_personas_guajira)
print("cantidad Personas Cañon Chicamocha:", cantidad_personas_canon_chicamocha)
print("cantidad Personas Llanos Orientales:", cantidad_personas_llanos_orientales)
print("total Dinero Guajira:", total_dinero_guajira)
print("total Dinero Cañon Chicamocha:", total_dinero_canon_chicamocha)
print("total Dinero LlanosOrientales:", total_dinero_llanos_orientales)
print("total Adultos:", total_adultos)
print("total Niños:", total_ninos)
print("total Dinero:", total_dinero)