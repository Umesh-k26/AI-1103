import matplotlib.pyplot as plt
import numpy as np

def F(x):
    if(x>=0 and x<1/2):
        return (1/2)*(x)**2
    elif(x>1/2 and x<=1):
        return (1/8) + (7/8)*(2*x - 1)**3
    elif(x>1):
        return 1

X = np.linspace(0,1,1000000)

Y = [F(x) for x in X]

plt.plot(X,Y)
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.title('Cumulative Distribution Function')
plt.show()
