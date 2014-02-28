from __future__ import print_function
import numpy as np
import itertools as it 


np.random.seed(3)
seq = "SMRT"
L = len(seq)
N = 10
# Use number 0,1,2,3 as S,M,R,T
Table = np.random.random_integers(0,L-1,size=(N,N))
Table2 = np.chararray((N,N))
Result = []
for i in range(N):
    for j in range(N):
        Table2[i,j] = seq[Table[i,j]]
np.savetxt("smrt.txt", Table2, fmt="%s")

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
