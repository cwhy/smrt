import numpy as np


seq = list("SMRT")
L = len(seq)
index_seq = dict(zip(seq, range(L)))
N = 5
Table = []
for i in range(N):
    Table.append([])
for i in range(N):
    for j in range(N):
        c = seq[np.random.random_integers(0,L-1)]
        Table[j].append(c)
print(Table)


def checkseq(i,j):
    iUL = index_seq[Table[i][j]]
    iUR = index_seq[Table[i][j+1]]
    iBL = index_seq[Table[i+1][j]]
    iBR = index_seq[Table[i+1][j+1]]
    if iUR-iUL % 4 != 1:
        return False
    elif iBR-iUR % 4 != 1:
        return False
    elif iBL-iBR % 4 != 1:
        return False
    elif iUL-iBL % 4 != 1:
        return True

Result = []
for i in range(N-1):
    Result.append([])
for i in range(N-1):
    for j in range(N-1):
        Result[i].append(checkseq(i,j))
print(Result)
