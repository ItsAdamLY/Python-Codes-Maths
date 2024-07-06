import PDEFiniteDiff as fd
import PDEBVF as bvf
import numpy as np

a,b,c,d = 1, 2, 1, 2
h=0.1
k=0.1;
m=(b-a)/h
n=(d-c)/k
f = lambda x,y: x/y + y/x;
g = bvf.PoissonBVF()
u = lambda x,y: x*y*np.log(x*y)

[x1,y1,w1] = fd.PoissonSolverh(f, g, a, b, c, d, h, k)
X,Y = np.meshgrid(x1,y1)
u(X,Y)

# [x2,y2,w2] = fd.PoissonSolverh(f, g, a, b, c, d, h/2, k/2)
# [x3,y3,w3] = fd.PoissonSolverh(f, g, a, b, c, d, h/4, k/4)

# print(str(x1) + " "*10 + str(w1) + "\n")
# print(str(x2[::2]) + " "*10 + str(w2[::2,::2]) + "\n")
# print(str(x3[::4]) + " "*10 + str(w3[::4,::4]))

# ext1 = (4*w2[::2,::2]-w1)/3
# ext2 = (4*w3[::4,::4]-w2[::2,::2])/3
# ext3 = (16*ext2-ext1)/15

#[X,Y] = np.meshgrid()