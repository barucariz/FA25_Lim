import numpy as np
import matplotlib.pyplot as plt

# 3-phase

pi = np.pi 

x = np.linspace(0,5*pi,100)
y1 = np.sin(x + pi/3)
y2 = np.sin(x + 2*pi/3)
y3 = np.sin(x + pi)

plt.figure(1)
plt.plot(x,y1,'b-')
plt.plot(x,y2,'r-')
plt.plot(x,y3,'k-')
plt.grid(True)
plt.show()


