import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 200)
y = np.zeros(len(x))

labels = ['Zeroth Order', 'Secondth Order', 'Fourth Order', 'Sixth Order']

plt.figure(figsize = (10,8))
for n, label in zip(range(4), labels):
    y = y + ((-1)**n * (x)**(2*n)) / np.math.factorial(2*n)
    plt.plot(x,y, label = label)

plt.plot(x, np.cos(x), 'k', label = 'Analytic Cosine') ##actual graph
plt.grid()
plt.title('Taylor Series Approximations of Various Orders')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


x = np.pi/2
y = 0
z = 0
s = 0

for n in range(4): #note how 4 is equivalent to the 7th degree polynomial for sin(x) as n=3 is the final entry
    y = y + ((-1)**n * (x)**(2*n)) / np.math.factorial(2*n)

print(y)