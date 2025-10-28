import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Cargar dataset
datos = sns.load_dataset('iris')

# Gráfico de dispersión
sns.scatterplot(data=datos, x='sepal_length', y='sepal_width')
plt.title('Gráfico de dispersión: longitud del sépalo vs ancho')
plt.xlabel('sepal_length')
plt.ylabel('sepal_width')
plt.show()

# Gráfico de barras
sns.barplot(data=datos, x='species', y='sepal_length')
plt.title('Gráfico de barras: longitud del sépalo por especie')
plt.xlabel('species')
plt.ylabel('sepal_length')
plt.show()

# Histograma
sns.histplot(datos['sepal_length'], bins=5)
plt.title('Histograma de longitud del sépalo')
plt.xlabel('sepal_length')
plt.ylabel('count')
plt.show()

# Gráfico de violín
sns.violinplot(data=datos, x='species', y='sepal_length')
plt.title('Gráfico de violín')
plt.xlabel('species')
plt.ylabel('sepal_length')
plt.show()

# Pairplot
sns.pairplot(data=datos, hue='species')
plt.show()

# Heatmap de correlaciones
corr = datos.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Mapa de calor de las correlaciones')
plt.show()