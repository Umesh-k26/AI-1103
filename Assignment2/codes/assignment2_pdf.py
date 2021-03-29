import matplotlib.pyplot as plt
import numpy as np

def f(x):
    if(x>=0 and x<1/2):
        return x
    elif(x>1/2 and x<=1):
        return 5.25*(2*x - 1)*(2*x -1)
    else:
        return 0

X = np.linspace(0,1,1000000)

Y = [f(x) for x in X]

plt.plot(X,Y)
plt.xlabel('$x$')
plt.ylabel('$f_X(x)$')
plt.title('Probability density function')
plt.show()
