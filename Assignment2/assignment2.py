import matplotlib.pyplot as plt
import numpy as np

def f(x):
    if(x>=0 and x<1/2):
        return x
    elif(x>1/2 and x<=1):
        return 5.25*(2*x - 1)*(2*x -1)
    else:
        return 0

x = np.arange(-2., 5., 0.001)

y = []

for i in range(len(x)):
   y.append(f(x[i]))

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Probability density function')

plt.plot(x,y,c='red', ls='', ms=1, marker='.')
ax = plt.gca()
ax.set_ylim([0, 8])

plt.show()
