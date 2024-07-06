import numpy as np
from numpy.linalg import solve
import matplotlib.pyplot as plot

def PoissonSolverh(f,g,xl,xr,yb,yt,h,k):
    
    M = (xr-xl)/h
    N = (yt-yb)/k
    
    return PoissonSolver(f, g, xl, xr, yb, yt, M, N)

def PoissonSolver(f,g,xl,xr,yb,yt,M,N):
    
    M,N = int(M),int(N)
    
    g1,g2,g3,g4 = g
    
    m,n = M+1, N+1
    mn = m*n
    h = (xr-xl)/M
    k = (yt-yb)/N
    
    h2, k2 = h**2, k**2
    
    A = np.zeros([mn,mn])
    b = np.zeros([mn,1])
    
    x = np.linspace(xl,xr,m)
    y = np.linspace(yb,yt,n)
    
    for i in range(1,M):
        for j in range(1,N):
    
            A[i+j*m][i-1+j*m]=1/h2
            A[i+j*m][i+1+j*m]=1/h2
            
            A[i+j*m][i+j*m]=-2/h2-2/k2
            
            A[i+j*m][i+(j-1)*m]=1/k2
            A[i+j*m][i+(j+1)*m]=1/k2
            
            b[i+j*m]=f(x[i],y[j])
    
    # Bottom and Top Boundary values
    for i in range(0,m):
        A[i][i] = 1
        b[i]    = g1(x[i])
        
        A[i+(n-1)*m][i+(n-1)*m] = 1
        b[i+(n-1)*m] = g2(x[i])
        
    for j in range(1,N):
        A[j*m][j*m] = 1
        b[j*m]    = g3(y[j])
       
        A[m-1+j*m][m-1+j*m] = 1
        b[m-1+j*m] = g4(y[j])
        
    print(b)
    print(np.size(b))
    v = solve(A,b)
    
    w = np.reshape(v, (m,n))
    X, Y = np.meshgrid(x, y)

    # Plotting
    fig = plot.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, w, cmap='viridis')
    plot.show()
    
    return [x,y,w.T]

#def meshplot(x,y,v):
    

#def HyperbolicSolver(f, g, ):