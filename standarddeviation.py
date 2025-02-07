import numpy as np

speed = [86,87,88,86,87,85,86]

sd = np.std(speed)
print(sd) #standard deviation low

speed = [32,111,138,28,59,77,97]

x = np.std(speed) #standard deviation high

#print(x)

#percentile
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
p = np.percentile(ages, 90) #fórmula para calcular o percentil --> posição = (n, número de dados * p, percentil desejado em %) / 100
print (p)