from __future__ import print_function
import numpy as np
import itertools as it 


N = 10
seq = "SMRT"
L = len(seq)
index_seq = dict(zip(seq, range(L)))
Table = np.readtxt(seq+".txt")
print(Table)
Result = []
# Use number 0,1,2,3 as S,M,R,T

def check(iUL,iUR,iBL,iBR):
    if iUR-iUL % 4 != 1:
        return False
    elif iBR-iUR % 4 != 1:
        return False
    elif iBL-iBR % 4 != 1:
        return False
    elif iUL-iBL % 4 != 1:
        return True
        
coords = list(it.product(range(N-1), range(N-1)))
for (i,j) in coords:
    iUL = Table[i,j]
    iUR = Table[i,j+1]
    iBL = Table[i+1,j]
    iBR = Table[i+1,j+1]
    if check(iUL,iUR,iBL,iBR):
        Result.append((i,j))
print(Result)
