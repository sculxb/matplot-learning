#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 20:35:00 2017

@author: cris
"""
import numpy as np
import matplotlib.pyplot as plt

phonon_dos= open('../file/phonon.dos')

dos = np.array([])

for line in phonon_dos.readlines():
    line = line.split()
    dos = np.concatenate((dos,line))

#print dos   
dos = dos.reshape(3000,2)
dos = np.transpose(dos)

fig = plt.figure(figsize=(2.5,6.5))
dos=dos.astype(float)
ax = plt.plot(dos[1],dos[0],'-',color='k')
plt.fill(dos[1],dos[0],color = 'k',alpha = 0.4)
plt.axis([0,1,0,320])

ax=plt.gca()  
ax.yaxis.tick_right()
ax.set_xticks(np.linspace(0,1,5))  
ax.set_xticklabels(('0.00','0.25','0.50','0.75','1.00'),size=13)
ax.get_yaxis().set_tick_params(direction='in', width=1) 
plt.yticks(fontsize=17)
plt.text(0.2, 325,'Frequency(cm$^{-1}$)',size = 17)
#plt.yaxis.get_label().set_color(p2.get_color())

plt.savefig("../graph/ph-dos.png")
plt.show()