import numpy as np
from scipy.stats import binom

## No. of simulations 
simulation_length = 10000

## No. of Children
n = 2

## Probability of child being boy 
p = 0.5

## Binomial Distribution
data_binom = binom.rvs(n, p,size = simulation_length)


## Counting number of boys in each simulation
count_0 = count_1 = count_2 = 0

for i in range(simulation_length):
    if data_binom[i] == 0:
        count_0+=1
    elif data_binom[i] == 1:
        count_1+=1
    elif data_binom[i] == 2:
        count_2+=1

## Simuation probabilities of random variable X = {0, 1, 2} where X is no. of boys  
sim_prob_0 = count_0/simulation_length
sim_prob_1 = count_1/simulation_length
sim_prob_2 = count_2/simulation_length


### Pr(X = 2 | X>= 1) = Pr(X = 2)/(Pr(X = 1) + Pr(X = 2))
prob_sim = sim_prob_2/(sim_prob_1 + sim_prob_2)


##### Calculating probablilites theoritically #####
k = np.arange(3)


## Theoritical probabilities of random variable X = {0, 1, 2} where X is no. of boys using binom.pmf
data_theo = binom.pmf(k, n, p)
theo_prob_0 = data_theo[0]
theo_prob_1 = data_theo[1]
theo_prob_2 = data_theo[2]

### Pr(X = 2 | X>= 1) = Pr(X = 2)/(Pr(X = 1) + Pr(X = 2))
prob_theo = theo_prob_2/(theo_prob_1 + theo_prob_2)


##### Printing results #####
print("Probability using simulation : ")
print("P( X = 2 | X >= 1) = {0:.2f}".format(prob_sim))
print()

print("Theoritical probability : ")
print("P( X = 2 | X >= 1) = {0:.2f}".format(prob_theo))
