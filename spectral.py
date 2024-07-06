import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fftshift

n = 50
dx = 2*np.pi/n
x = np.arange(0, 2*np.pi, dx)
eta=0.5
h=0.1

alp = 1/16

psteps = 11 
tmax = h*(psteps-1) # psteps= time-slices to plot

step = np.arange(-n/2,n/2, 1)
nv = fftshift(step) # wave numbers
mu = (1-h*(1-eta)*alp*nv**2)/(1+eta*alp*nv**2*h) # F-multiplier vector

u0 = 2*np.sin(x)
u = u0
uf = np.fft.fft(u) # initial condition

t = np.arange(0,h*(psteps),h)
ua = np.zeros((psteps,n))

ua[0,:] = u0 # for plotting
for i in range(1,psteps): # integration loop
     uf = mu*uf
     u = np.fft.ifft(uf)
     ua[i,:] = np.real(u) # back to x only for plotting
     
X, T = np.meshgrid(x, t)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, ua, cmap='viridis')
plt.show()

actual_f = lambda x,t : 2*np.exp(-t/16)*np.sin(x)
print("Error between estimation and actual: " + str(abs(actual_f(X,T) - ua)))