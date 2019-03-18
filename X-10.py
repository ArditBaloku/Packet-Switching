import math

n = 35
k = 0
p = 0.1
q = 0.9
result = 0

for x in range(0, 11):
    result += math.factorial(n)/(math.factorial(n-k)*math.factorial(k))*math.pow(p,k)*math.pow(q,n-k)
    k += 1

print("Rezultati eshte: {}".format(1-result))