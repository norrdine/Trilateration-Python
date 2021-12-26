# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 19:17:07 2021

@author: A. Norrdine
Trilateration algorithm 
paper "An algebraic solution to the multilateration problem"
Author: Norrdine, Abdelmoumen  (norrdine@hotmail.de)
https://www.researchgate.net/publication/275027725_An_Algebraic_Solution_to_the_Multilateration_Problem
note : Interim results may differ from the paper (depends on the choise of Z = null(A)).
"""

import numpy as np
from scipy.linalg import null_space
from numpy.linalg import matrix_rank

def trilateration(P,S,W):
    m,n = P.shape
    ns = S.size
    A = np.zeros((n,4))
    b = np.zeros((n,1))
    if ns != n:
        raise ValueError('Number of reference points and distances are different')
    for i in range(n):
        x = P[0,i]
        y = P[1,i]
        z = P[2,i]
        s = S[i]
        A[i,:] = np.array([1, -2*x, -2*y, -2*z])
        b[i] = s**2-x**2-y**2-z**2
        #print('A = ' + str(A))
        #print('b = ' + str(b))
        #print('----------------')
        #inp = input('.')
    if (n==3):
        Ap = np.linalg.pinv(A) # pinv
        Xp =np.matmul(Ap,b) # particular solution
        xp = Xp.flatten()[1:]
        Z = null_space(A)
        z = Z.flatten()[1:]
        if matrix_rank(A)==3:
            a2 = z[0]**2 + z[1]**2 + z[2]**2 
            a1 = 2*(z[0]*xp[0] + z[1]*xp[1] + z[2]*xp[2])-Z.flatten()[0]
            a0 = xp[0]**2 +  xp[1]**2+  xp[2]**2-Xp.flatten()[0]
            polynom = [a2, a1, a0]
            t = np.roots(polynom)
            #Solutions
            N1 = Xp + t[0]*Z;
            N2 = Xp + t[1]*Z;
    if (n>3):
        #Xp = pinv(A)*b;
        Ap = np.linalg.pinv(A) # pinv
        Xp =np.matmul(Ap,b) # particular solution
    N1 = Xp
    N2 = N1
    if (matrix_rank(A)<4):
        Ap = np.linalg.pinv(A) # pinv
        Xp =np.matmul(Ap,b) # particular solution
        xp = Xp.flatten()[1:]
        Z = null_space(A)
        z = Z.flatten()[1:]
        a2 = z[0]**2 + z[1]**2 + z[2]**2 
        a1 = 2*(z[0]*xp[0] + z[1]*xp[1] + z[2]*xp[2])-Z.flatten()[0]
        a0 = xp[0]**2 +  xp[1]**2+  xp[2]**2-Xp.flatten()[0]
        polynom = [a2, a1, a0]
        t = np.roots(polynom)
        #Solutions
        N1 = Xp + t[0]*Z;
        N2 = Xp + t[1]*Z;
        pass
    #return N1, N2 
    return N1, N2