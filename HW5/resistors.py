import numpy as np

def main():
    #Constants 
    N = 10
    V_0 = 5

  # Set up the initial values of the arrays 
    A = np.zeros((N,N),float)
    for i in range(2, N-2):
        A[i,i-2] = -1
        A[i,i-1] = -1
        A[i,i] = 4
        A[i,i+1] = -1
        A[i,i+2] = -1
    
    #Set up boundary conditions
    A[0,0] = 3
    A[0,1] = -1
    A[0,2] = -1

    A[1,0] = -1
    A[1,1] = 4
    A[1,2] = -1
    A[1,3] = -1

    A[N-2,N-4] = -1
    A[N-2,N-3] = 4
    A[N-2,N-2] = -1
    A[N-2,N-1] = -1


    A[N-1,N-1] = 3
    A[N-1,N-2] = -1
    A[N-1,N-3] = -1

    v = np.zeros(N,float)
    v[0] = V_0
    v[1] = V_0

    rank_A = np.linalg.matrix_rank(A)
    print(rank_A)

    rank_v = np.linalg.matrix_rank(v)
    print(rank_v)

    print(A)

    w = np.linalg.solve(A,v)
    print(w)

if __name__ == "__main__":
    main()