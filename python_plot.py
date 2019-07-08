import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(0,2*np.pi,100)
f, ax = plt.subplots
ax.plot(x,np.sin(x))
