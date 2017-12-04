#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 19:45:21 2017

@author: cris
"""

#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif']=['Abyssinica SIL']
np.set_printoptions(threshold=np.NaN)

s_zero_point_zero_five = open('../file/TS444.freq.gp.sigma=0.1')
#s_zero_point_one = open('../file/TS444.freq.gp.sigma=0.1')
datalist = np.array([])
data = np.array([])
col = []

for line in s_zero_point_zero_five.readlines():
    line = line.split()
    data = np.concatenate((data,line))   
#print datalist[11]
#print data[11]
data = data.reshape(301,10)

col = np.transpose(data)

xx=col[0].astype(float)

fig = plt.figure(figsize=(9,6.5))
for i in range(1,10):
    yy = col[i].astype(float)
    plt.plot(xx,yy,color='k')

#add label    
plt.title(r'Phonon dispersion of monolayer TiSe${_2}$',size=25,y=1.02)
plt.ylabel(r'Frequency(cm$^{-1}$)',size=25)
plt.text(0.450933, -30,'$\Gamma$',size = 30)
plt.text(-0.0100, -30,'K',size = 30)
plt.text(0.935, -30,'M',size = 30)
plt.text(1.32, -30,'K',size = 30)
plt.axis([0,1.343462,0,320])
plt.xticks([])
plt.yticks(fontsize=20)

#add lengend
#plt.plot([0,0],'-',color='k',label='$\sigma$ =0.05Ry')
plt.plot([0,-10],'--',color='r',label='$\sigma$ =0.1Ry')
plt.legend(loc='bottom left',bbox_to_anchor=(1.01,0.1))
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize='xx-large')

#set ticks
ax = plt.gca()
ax.yaxis.set_ticks_position('left')
ax.get_yaxis().set_tick_params(direction='in', width=1)
plt.axvline(0.470933)
plt.axvline(0.970933)

plt.savefig("../graph/sigma-0.1Ry.png")
plt.show()
