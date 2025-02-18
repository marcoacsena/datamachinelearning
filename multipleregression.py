import pandas as pd
from sklearn import linear_model

df = pd.read_csv('data.csv')

x = df[['Weight', 'Volume']]
y = df['CO2']

regression = linear_model.LinearRegression()
regression.fit(x, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regression.predict([[2300, 1300]])

print(predictedCO2)
print(regression.coef_)



