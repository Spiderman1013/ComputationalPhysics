import numpy as np

def gaussianElimination(A,v):
    A= A.astype(float)
    v = v.astype(float)
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

def partialPivoting(A,v):
    A= A.astype(float)
    v = v.astype(float)
    N = len(v)

    #do partial pivoting
    for m in range(N):
        #find the row with the largest value in the mth column
        max_row = m
        for i in range(m+1,N):
            if abs(A[i,m]) > abs(A[max_row,m]):
                max_row = i
        #swap the rows
        A[[m,max_row]], A[[max_row,m]] = A[[max_row,m]], A[[m,max_row]]
        v[[m,max_row]], v[[max_row,m]] = v[[max_row,m]], v[[m,max_row]]
    
    return gaussianElimination(A,v)


def main():
    A = np.array([[0,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]])
    v = np.array([-4,3,9,7],dtype=float)
    x = partialPivoting(A,v)
    print(x)    

if __name__ == "__main__":
    main()