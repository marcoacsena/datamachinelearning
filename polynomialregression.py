import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Dados
x = np.array([30, 40, 50, 60, 70, 80, 90]).reshape(-1, 1)
y = np.array([18, 20, 22, 23, 22, 20, 18])

# Transforma x em características polinomiais (grau 2)
poly = PolynomialFeatures(degree=2)
x_poly = poly.fit_transform(x)

# Ajusta o modelo
model = LinearRegression()
model.fit(x_poly, y)

# Previsão
y_pred = model.predict(x_poly)

# Plot
plt.scatter(x, y, color='blue', label='Dados reais')
plt.plot(x, y_pred, color='red', label='Regressão polinomial')
plt.xlabel('Velocidade (km/h)')
plt.ylabel('Consumo (km/l)')
plt.legend()
plt.show()