from __future__ import print_function
import numpy as np


seq = list("SMRT")
L = len(seq)
index_seq = dict(zip(seq, range(L)))
N = 100
Table = []
for i in range(N):
    Table.append([])
for i in range(N):
    for j in range(N):
        c = seq[np.random.random_integers(0,L-1)]
        Table[j].append(c)
#for line in Table:
#    print(line,sep='\n')


def checkseq(i,j):
        return True

Result = []
for i in range(N-1):
    for j in range(N-1):
        iUL = index_seq[Table[i][j]]
        iUR = index_seq[Table[i][j+1]]
        iBL = index_seq[Table[i+1][j]]
        iBR = index_seq[Table[i+1][j+1]]
        if iUR-iUL % 4 != 1:
            continue
        elif iBR-iUR % 4 != 1:
            continue
        elif iBL-iBR % 4 != 1:
            continue
        elif iUL-iBL % 4 != 1:
            Result.append((i,j))
print(Result)
