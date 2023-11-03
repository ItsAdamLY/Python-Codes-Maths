import numpy as np

def NormalEqSolve (n, x, y): ## with =, is returning a value
    
    SumMat = np.zeros((n+1,n+1))
    SumMat_xy = np.zeros((n+1, 1))

    for row in range (0, n+1):
        for col in range (0, n+1):
            k = (row+1)+(col+1)-2
            SumMat[row,col] = np.sum(x**k)
            SumMat_xy[row] = np.sum(y*(x**(row)))
    
    return [SumMat, SumMat_xy]