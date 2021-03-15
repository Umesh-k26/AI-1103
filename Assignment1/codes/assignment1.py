# 0 corresponds to (girl, girl)
# 1 corresponds to (boy, girl) or (girl, boy)
# 2 corresponds to (boy, boy)

import random as rd
simulation_length = 10000

# random variable X = {0, 1, 2} count for no. of boys
X_0_count = X_1_count = X_2_count = 0

sample_space = ["GG", "BG", "GB", "BB"]
for i in range(simulation_length):
    temp = rd.randint(0, 3)

    #conditions in "if ladder" are w.r.t. to indices in sample_space list.
    if(temp == 0):
        X_0_count += 1
    elif(temp == 1 or temp == 2):
        X_1_count += 1
    else:
        X_2_count += 1

X_0_prob = X_0_count/simulation_length
X_1_prob = X_1_count/simulation_length
X_2_prob = X_2_count/simulation_length


# To find the probablity of two boys given atleast one of them is a boy
# By Bayes Theorem P(X=2 | X >= 1) = P(X=2) / P(X >= 1)
#  P(X >= 1) = P(X=1) + P(X=2)

X_1_or_2_prob = X_1_prob + X_2_prob

simulation_result = X_2_prob / X_1_or_2_prob

print("Theoritical probabilities :")
print("P(X = 0) = 0.25")
print("P(X = 1) = 0.50")
print("P(X = 2) = 0.25")
print("P( X = 2 | X >= 1) = 0.33")
print()

print("Probabilites using simulation : ")
print("P(X = 0) = {0:.2f}".format(X_0_prob))
print("P(X = 1) = {0:.2f}".format(X_1_prob))
print("P(X = 2) = {0:.2f}".format(X_2_prob))
print("P( X = 2 | X >= 1) = {0:.2f}".format(simulation_result))
