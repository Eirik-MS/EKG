import numpy as np
import matplotlib.pyplot as plt


#solve differential equation for simple EKG


#define constants
a = 0
b = 0
c = 0

def v_dot(v, w):
    return (v-a)*(1-v)*v - w

def w_dot(v, w):
    return b*c-c*w

#initial conditions

t = np.linspace(0, 200, 2000)
V_e = np.zeros(len(t))

#solve with newton's method
for i in range(1, len(t)):
    

