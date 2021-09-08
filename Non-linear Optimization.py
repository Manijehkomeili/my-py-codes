"""
Created on Tue Sep  7 12:17:44 2021

This is a sample Nonlinear Optimization
Objective function:

     Min x3 + (x1 + x2 + x3) * x1 * x2 * x4

      s.t. x1 * x2 * x3 * x4 >= 25
     (x1)^2 + (x2)^2 + (x3)^2 + (x4)^2 = 40

   Bounds:  1 <= x1, x2, x3, x4 <= 5
   Initial guess  x0 = (2,4,4,2)

@author: Manijeh Komeili
"""

import numpy as np
from scipy.optimize import minimize


def objective(x):
    return x[0] + (x[0] + x[1] + x[2]) * x[0] * x[1] * x[3]


def constraint1(x):
    return x[0] * x[1] * x[2] * x[3] - 25.0


def constraint2(x):
    sum_eq = 40.0
    for i in range(4):
        sum_eq = sum_eq - x[i] ** 2
    return sum_eq


# initial guesses
n = 4
x0 = np.zeros(n)
x0[0] = 2.0
x0[1] = 4.0
x0[0] = 4.0
x0[1] = 2.0

# show initial objective
print('Initial Objective: ' + str(objective(x0)))

# optimize
bnd = (1.0, 5.0)
bnds = (bnd, bnd, bnd, bnd)
const1 = {'type': 'ineq', 'fun': constraint1}
const2 = {'type': 'eq', 'fun': constraint2}
consts = ([const1, const2])
solution = minimize(objective, x0, method='SLSQP', bounds=bnds, constraints=consts)
x = solution.x

# show final objective
print('Final Objective: ' + str(objective(x)))

# print solution
print('Solution')
print('x1 = ' + str(x[0]))
print('x2 = ' + str(x[1]))
print('x3 = ' + str(x[2]))
print('x4 = ' + str(x[3]))
