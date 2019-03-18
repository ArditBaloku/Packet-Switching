import matplotlib.pyplot as plt
import math
x = []
y = []
for i in range(0, 35):
    x.append(i+1)
for j in range(0, 35):
    y.append((math.factorial(35)/(math.factorial(35-j)*math.factorial(j)))*math.pow(0.1, j)*math.pow(0.9, 35-j))
plt.plot(x , y, 'ro')
plt.show()

# z = 0
# for i in range(11 , 35):
#     x.append(i+1)
# for j in range(11, 35):
#     z += (math.factorial(35)/(math.factorial(35-j)*math.factorial(j)))*math.pow(0.1, j)*math.pow(0.9, 35-j)
#     y.append(z)
# plt.plot(x , y, 'ro')
# plt.show()