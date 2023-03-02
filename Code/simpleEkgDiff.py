import numpy as np
import matplotlib.pyplot as plt


#solve differential equation for simple EKG


#define constants
a = 0.2
b = 1
c = 0.04

def v_dot(v, w):
    return (v-a)*(1-v)*v - w

def w_dot(v, w):
    return (b*c)-(c*w)

#initial conditions

t = np.linspace(0, 200, 50)
V_e = np.zeros(len(t))
W_e = np.zeros(len(t))

V_e[0] = 0.55
W_e[0] = 0

#solve with newton's method
for i in range(1, len(t)):
    V_e[i] = V_e[i-1] + v_dot(V_e[i-1], W_e[i-1])
    for i in range(1, 10):
        W_e[i] = W_e[i-1] + w_dot(V_e[i-1], W_e[i-1])



plt.plot(t, V_e, 'r', label='V')
plt.scatter(t[3], V_e[3], label='A', color='black')
plt.scatter(t[10], V_e[10], label='B', color='blue')
plt.scatter(t[12], V_e[12], label='C', color='green')
plt.legend()
plt.show()
