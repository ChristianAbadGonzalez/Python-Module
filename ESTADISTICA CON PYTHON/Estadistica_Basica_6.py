import numpy as np
import matplotlib.pyplot as plt

# Parámetros
num_neuronas = 100
lambda_poisson = 0.5
num_iteraciones = 1000

# Simular el número de neuronas desactivadas por iteración
# Cada neurona se desactiva según Poisson(lambda_poisson); sumamos en cada iteración
neurons_off_counts = []
rng = np.random.default_rng()  # generador moderno

for _ in range(num_iteraciones):
    # Genera, para 100 neuronas, 100 muestras Poisson(lambda)
    dropout_mask = rng.poisson(lam=lambda_poisson, size=num_neuronas)
    num_neurons_off = dropout_mask.sum()
    neurons_off_counts.append(num_neurons_off)

# Número medio de neuronas desactivadas
mean_neurons_off = np.mean(neurons_off_counts)
print(f'Número medio de neuronas desactivadas en {num_iteraciones} iteraciones: {mean_neurons_off:.2f}')

# Histograma
plt.hist(neurons_off_counts, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
plt.title('Distribución de Neuronas Desactivadas en 1000 Iteraciones')
plt.xlabel('Número de Neuronas Desactivadas')
plt.ylabel('Frecuencia')
plt.show()