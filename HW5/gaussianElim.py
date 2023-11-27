import numpy as np

# Define a function to perform Gaussian elimination for Ax = v
def gaussianElimation(A,v):
    N = len(v)

    for m in range(N):
        # Divide by the diagonal element
        div = A[m,m]
        A[m,:] /= div
        v[m] /= div

        # Subtract from the lower rows
        for i in range(m+1,N):
            mult = A[i,m]
            A[i,:] -= mult*A[m,:]
            v[i] -= mult*v[m]
    
    #Back substitution
    x = np.zeros(N)
    for m in range(N-1,-1,-1):
        x[m] = v[m]
        for i in range(m+1,N):
            x[m] -= A[m,i]*x[i]
    return x

