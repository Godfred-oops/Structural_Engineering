# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 14:50:35 2022

@author: Quophi_ababio
"""

import numpy as np
import matplotlib.pyplot as plt 
x = [38.75,-20,-20,-20,21.25]
y = [0,0,2,2,4,4]
p = 0
e = [p]

for i in range(len(x)):
    p = p + x[i]
    e.append(p)

print(e)
plt.plot(y,e)
plt.plot([0,4], [0,0])

for a,d in zip(y,e):
    plt.annotate(np.round(d,2), (a,d), horizontalalignment = 'left',
                 verticalalignment = 'top', fontsize = 9)



