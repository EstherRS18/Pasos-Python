import pandas as pd

data = {'Nombre': ['Esther', 'Gerald', 'Wilian', 'Jorge'],
        'Edad': [25, 30, 22, 28],
        'Puntuación': [80, 92, 88, 78]}

df = pd.DataFrame(data)

filtro_edad = df['Edad'] > 25
resultados = df[filtro_edad]

print(resultados)
