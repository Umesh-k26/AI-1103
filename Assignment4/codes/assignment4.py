from scipy.stats import norm

sim_len = 10000
count1 = count2 = count3 = 0

for i in range(sim_len):
    X1 = norm.rvs()
    X2 = norm.rvs()
    X3 = norm.rvs()
    X4 = norm.rvs()
    X5 = norm.rvs()

    if X2 == max(X2, X3, X4, X5):
        count1 += 1
    if X3 == max(X3, X4, X5):
        count2 += 1
    if X4 == max(X4, X5):
        count3 += 1

print("Experimental probability = ", (count1/sim_len)*(count2/sim_len)*(count3/sim_len))
print("Theoritical probability = ", 1/24)
