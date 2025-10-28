# Importación y uso de librerias
import pandas as pd
import numpy as np

# Acceso e inportación de archivos csv
df = pd.read_csv('salary_data.csv', sep = ";")


# Calculo del rango
Rango = (df.income.max() - df.income.min())
print(Rango)

rango_numpy = (np.max(df.age) - np.min(df.age))
print(rango_numpy)


# Calculo de la varianza

Varianza = df.age.var()
print('media', df.age.mean())
print('Varianza Edad', (Varianza))

Varianza_np = np.var(df.age)
print('Varianza Numpy Edad', (Varianza_np))

print('VARIANZAS POBLACIONALES')

Varianza = df.age.var(ddof = 0)
print('Varianza Edad', Varianza)

Varianza_np = np.var(df.age, ddof = 0)
print('Varianza Numpy Edad', Varianza_np)


# Desviacion estandar

ds = df.age.std()
print('Desviacion Estandar', ds)

ds_np = np.std(df.age)
print('Desviacion Numpy Estandar', ds_np) # Desviacion estandard numpy

ds = df.age.std()
print('Desviacion Estandar',ds)

ds_np = np.std(df.age)
print('Desviacion Numpy Estandar',ds_np)