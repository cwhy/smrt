from __future__ import print_function
import numpy as np
import itertools as it 


np.random.seed(3)
def generate(seq,N):
    L = len(seq)
    Table = np.random.random_integers(0,L-1,size=(N,N))
    Table2 = np.chararray((N,N))
    for i in range(N):
        for j in range(N):
            Table2[i,j] = seq[Table[i,j]]
    np.savetxt(seq + ".txt", Table2, fmt="%s")


generate("SMRT",100)
generate("FISHEAD",10000)
