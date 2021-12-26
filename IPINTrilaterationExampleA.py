# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 20:13:16 2020

@author: A. norrdine

Test Trilateration algorithm 
paper "An algebraic solution to the multilateration problem"
Author: Norrdine, Abdelmoumen  (norrdine@hotmail.de)
https://www.researchgate.net/publication/275027725_An_Algebraic_Solution_to_the_Multilateration_Problem
note : Interim results may differ from the paper (depends on the choise of Z = null(A)).
Numerical example: A. Solution based on three reference points: 
"""

import numpy as np
from trilateration import trilateration

print('Trilateration example: A')
 
#Reference points
P1 = np.array([	27.297,	-4.953,	1.47])
P2 = np.array([	25.475,	-6.124,	2.36])
P3 = np.array([	22.590,	0.524,	1.2])
#distances
s1 = 3.851  # distance to P1
s2 = 3.875 # distance to P2
s3 = 3.514 # distance to P3

P = np.array([P1, P2, P3] ) # Reference points matrix
P = np.column_stack([P1, P2, P3])
S = np.array([s1, s2, s3]) # Distance vector
W = np.eye(3)  # Weigths matrix


N1, N2 = trilateration(P,S,W)

print('Solution:')
print(f"N1 = {N1[1:].flatten()}")
print(f"N2 = {N2[1:].flatten()}")

print('Quality factor:')
q = N1[0]-(N1[1]**2 + N1[2]**2 + N1[3]**2)
print(f"q = {q}")
