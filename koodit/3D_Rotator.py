import matplotlib.pyplot as plt
import numpy as np
                                
fig = plt.figure()              #Creating Figure
ax = plt.axes(projection='3d')  #Creating the axis

Fs = 1000                       #Samples
Ts = 1/Fs                       #Samples per second
t = np.arange(0,10,Ts)          #Time
f = 1                           #Frequency
j = complex(0,1)                #Magic???
s = np.exp(j*2*np.pi*f*t)       #Signal

z = t                           #Mapping time to Z
x = np.real(s)                  #Mapping real part to X
y = np.imag(s)                 #Mapping imaginary part to Y
ax.plot3D(x,y,z, 'red')         #Plotting
fig.suptitle('3D')              #Setting subtitle fot the plot

plt.show()                      