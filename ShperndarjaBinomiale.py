import math

n = 35
k = 0
p = 0.1
q = 0.9

for x in range(0, 36):
    print("Shperndarja binomiale per k = {}".format(x))
    print(math.factorial(n)/(math.factorial(n-k)*math.factorial(k))*math.pow(p,k)*math.pow(q,n-k))
    k += 1
