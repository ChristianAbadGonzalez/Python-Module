import math

def norm_cdf(x, mu=0.0, sigma=1.0):
    # CDF de la normal N(mu, sigma) usando la función error
    z = (x - mu) / (sigma * math.sqrt(2))
    return 0.5 * (1 + math.erf(z))

# Parámetros de la distribución normal
mu = 170   # Media
sigma = 12 # Desviación estándar

# Definir los límites del intervalo
x1 = 189   # Límite inferior del intervalo
x2 = 190   # Límite superior del intervalo

# Calcular la probabilidad P(x1 < X < x2) donde X ~ N(mu, sigma)
prob = norm_cdf(x2, mu, sigma) - norm_cdf(x1, mu, sigma)

# Imprimir el resultado
print(f"La probabilidad de que un alumno mida entre {x1} cm y {x2} cm es aproximadamente {prob*100:.4f} %")