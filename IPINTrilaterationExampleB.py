# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 20:13:16 2020

@author: A. norrdine

Test Trilateration algorithm 
paper "An algebraic solution to the multilateration problem"
Author: Norrdine, Abdelmoumen  (norrdine@hotmail.de)
https://www.researchgate.net/publication/275027725_An_Algebraic_Solution_to_the_Multilateration_Problem
note : Interim results may differ from the paper (depends on the choise of Z = null(A)).
Numerical example: B. Solution based on three reference points: 
"""

import numpy as np

from trilateration import trilateration

print('Trilateration example: B')
#Reference points
P37 = np.array([	27.297,	-4.953,	1.47])
P31 = np.array([	20.693,	-4.849,	1.93])
P102 = np.array([	22.590,	0.524,	1.2])
P43 = np.array([	17.113,	-3.003,	2.17])
P208 = np.array([	22.554,	4.727,	1.77])
P101 = np.array([	22.447,	-7.880,	1.6])

#distances
s1 = 3.851  # distance to P1
s2 = 3.875 # distance to P2
s3 = 3.514 # distance to P3

P = np.column_stack([P37, P31, P102, P43, P208, P101] ) # Reference points matrix
#P = np.column_stack([P1, P2, P3])
S = np.array([3.6520, 7.0360, 4.5860, 9.8400, 7.4020, 7.8830]) # Distance vector
W = np.eye(6) # Weigths matrix


N1, N2 = trilateration(P,S,W)

print('Solution:')
print(f"N1 = {N1[1:].flatten()}")


print('Quality factor:')
q = N1[0]-(N1[1]**2 + N1[2]**2 + N1[3]**2)
print(f"q = {q}")
