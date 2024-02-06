from datetime import datetime

print('////BIENVENIDO AL SISTEMA DE PARQUEADEROS GALVIS////')
print('----------------------------------------------------')

# Ingresa la cantidad de parqueaderos para carros y motos
camp_cars = int(input('Ingresa la cantidad de parqueaderos para carros: '))
camp_motorcycles = int(input('Ingresa la cantidad de parqueaderos para motos: '))

# Define los campos del parqueadero
name_camp_cars = [{'place': str(input('Ingresa el nombre del campo del parqueadero de carro: ')), 'available': True} for
                  _ in range(camp_cars)]
name_camp_moto = [{'place': str(input('Ingresa el nombre del campo del parqueadero de moto: ')), 'available': True} for
                  _ in range(camp_motorcycles)]

# Define tarifas de cobro por tiempo
cost_frac_car = 2000
cost_frac_moto = 1000

# Registra la entrada o salida de vehículos
register_car = []
register_motorcycle = []

while True:
    # Recorre un for dentro de una lista para consultar los diccionarios que hay
    place_free_moto = [x['place'] for x in name_camp_moto if x['available']]
    place_free_car = [x['place'] for x in name_camp_cars if x['available']]

    print('Lugares disponibles:', place_free_car, place_free_moto)

    print('¿QUÉ OPCIÓN DESEAS REALIZAR?')
    options = input('1. Registrar nuevo vehículo \n2. Registrar salida de vehículo\nOpción >: ')

    # Validar que el dato no sean letras
    if not options.isdigit() or options not in {'1', '2'}:
        print('NO SE ADMITEN LETRAS, SOLO LAS OPCIONES 1 o 2')

    # Opción para registrar Moto o Carro
    elif options == '1':
        if len(place_free_moto) > 0 or len(place_free_car) > 0:
            tipo_vehiculo = input('¿Qué tipo de vehículo deseas registrar (moto o carro)? ').lower()
            if tipo_vehiculo == 'moto':
                # Registrar entrada de moto
                moto = place_free_moto.pop()
                moto['available'] = False
                register_motorcycle.append({'place': moto['place'], 'entry_time': datetime.now()})
                print(f'Moto registrada en el lugar {moto["place"]}')
            elif tipo_vehiculo == 'carro':
                # Registrar entrada de carro
                carro = place_free_car.pop()
                carro['available'] = False
                register_car.append({'place': carro['place'], 'entry_time': datetime.now()})
                print(f'Carro registrado en el lugar {carro["place"]}')
            else:
                print('Opción no válida. Ingresa "moto" o "carro".')
        else:
            print('No hay lugares disponibles.')
