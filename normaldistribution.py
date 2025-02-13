import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(5.0, 1, 100000) #distribuição normal, também conhecida como distribuição de dados Gassiana
                                         #5 representa o valor médio,1 o desvio padrão, e 100.000 a quantidade de números

plt.hist(x, 5)
plt.show()
