# Impliment 4th Order Runge-Kutta method


# y(n+1) = y(n) + (1/6)(k(1) + 2k(2) + 2k(3) + k(4))
# y' = f(x, y)
# x(n + 1) = x(n) + h
#k(1) = h * f(x(n), y(n))
#k(2) = h * f(x(n) + h/2, y(n) + k(1)/2)
#k(3) = h * f(x(n) + h/2, y(n) + k(2)/2)
#k(4) = h * f(x(n) + h, y(n) + k(3))

import math
import sys

x_n = float(raw_input("Please enter the x of n: "))
y_n = float(raw_input("Please enter y's value at n: "))
h = float(raw_input("Please enter the step size: "))
steps = int(raw_input("Please enter the number of steps: "))
func = raw_input("Using correct python syntax please enter y prime in terms of x and y: ")

def y_prime (x, y, func): return eval(func)

for i in range(steps):
    k1 = h * y_prime(x_n, y_n, func)
    k2 = h * y_prime((x_n + h/2), y_n + k1/2, func)
    k3 = h * y_prime((x_n + h/2), y_n + k2/2, func)
    k4 = h * y_prime(x_n + h, y_n + k3, func)
    y_n = y_n + (1.0/6.0)*(k1 + 2*k2 + 2*k3 + k4)
    x_n += h
    print 'y[{0}] = {1}'.format(x_n, y_n)
