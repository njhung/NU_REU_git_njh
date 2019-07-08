# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2*np.pi,100)
f, ax = plt.subplots()
ax.plot(x,np.cos(x))
ax.set_xlabel('x')
ax.set_ylabel('y')
