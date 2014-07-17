from __future__ import division
#This is the solution under Numbers category for project https://github.com/hsssgddtc/Basis-Training
""" Find out the value of Pi use below formulas: Pi = 4 * (1/1 - 1/3 + 1/5 - 1/7 + ...),
until the absolute value of the last item less than 0.00000001"""

Pi = 0
for N in range(1,10000000):
    Pi += 4 * 1/(2*N-1) * pow(-1,N-1)

print Pi
    

