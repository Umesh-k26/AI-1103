import math 

import numpy as np
import matplotlib.pyplot as plt 
from scipy.stats import bernoulli
from scipy.stats import norm 
from scipy.stats import binom

#number of test cases
k = 50000
Pr_A= 4/52
Pr_B = 4/52

Top_ace = bernoulli.rvs(size = k, p = Pr_A)

Bottom_ace = bernoulli.rvs(size = k, p = Pr_B)


Both_aces = 0
for i in Top_ace:
    if i == 1:
        for j in Bottom_ace:
            if j == 1:
                Both_aces += 1
        
prob_Both_aces = Both_aces/(k*k)

print("The probability is: ", prob_Both_aces)

#plotting

cases = ['']

probab_theo = (3*4)/(51*52)
probab_sim = prob_Both_aces

#plt.figure(figsize=(24,16))
#plt.subplots_adjust(left = None, bottom = 0, right = None, top = 1, wspace = None, hspace = None )
x = np.arange(len(cases))
plt.bar(x + 0.00, probab_theo, color = 'b', width = 0.2, label = 'Theoretical')
plt.bar(x + 0.2, probab_sim, color = 'g', width = 0.2, label = 'Simulated')
plt.xlabel('Theoretical v/s Simulated')
plt.ylabel('Probability')
plt.xticks(x  + 0.2/2,[''])


a = np.arange(0,0.9,0.001)
plt.yticks(a)
plt.ylim([0, 0.01])
#plt.margins(0.01)
plt.grid(b = True, color ='black',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)

plt.legend()
plt.show()