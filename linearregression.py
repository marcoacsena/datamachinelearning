import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6] #ages
y = [99,86,87,88,111,86,103,87,94,78,77,85,86] #speed

slop, intercept, r, p, std_er = stats.linregress (x, y)

def myfunct (x):
    
    return (slop * x + intercept)#é a equação linear: y = A(slop)X + B(intercept).É o valor de Y na equação

mymodel = list(map(myfunct, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()


