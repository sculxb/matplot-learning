#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif']=['Abyssinica SIL']
np.set_printoptions(threshold=np.NaN)

#initialize parameter
s_zero_point_zero_five = open('../file/TS444.freq.gp.sigma=0.05')
s_zero_point_one = open('../file/TS444.freq.gp.sigma=0.1')
s_zero_point_one_five = open('../file/TS444.freq.gp.sigma=0.15')
s_zero_point_two = open('../file/TS444.freq.gp.sigma=0.2')
datalist = np.array([])
data = np.array([])
sigma_xx = np.array([])
sigma_yy = np.array([])
sigma_zz = np.array([])
col = []

for line in s_zero_point_zero_five.readlines():
    line = line.split()
    data = np.concatenate((data,line))

for line in s_zero_point_one.readlines():
    line = line.split()
    sigma_xx = np.concatenate((sigma_xx,line))

for line in s_zero_point_one_five.readlines():
    line = line.split()
    sigma_yy = np.concatenate((sigma_yy,line))    

for line in s_zero_point_two.readlines():
    line = line.split()
    sigma_zz = np.concatenate((sigma_zz,line))

print data
#print data[11]
data = data.reshape(301,10)
col_xx = sigma_xx.reshape(301,10)
col_yy = sigma_yy.reshape(301,10)
col_zz = sigma_zz.reshape(301,10)

col = np.transpose(data)
col_xx = np.transpose(col_xx)
col_yy = np.transpose(col_yy)
col_zz = np.transpose(col_zz)


x_axis=col[0].astype(float)

fig = plt.figure(figsize=(9,6.5))
for i in range(1,10):
    one = col[i].astype(float)
    two = col_xx[i].astype(float)
    three = col_yy[i].astype(float)
    four = col_zz[i].astype(float)
    plt.plot(x_axis,one,color='k')
    plt.plot(x_axis,two,'--',color='r')
    plt.plot(x_axis,three,'-.',color='b')
    plt.plot(x_axis,four,':',color='y')

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
plt.plot([0,0],'-',color='k',label='$\sigma$ =0.05Ry')
plt.plot([0,0],'--',color='r',label='$\sigma$ =0.1Ry')
plt.legend(loc='bottom left',bbox_to_anchor=(1.01,0.164))
leg = plt.gca().get_legend()
ltext  = leg.get_texts()
plt.setp(ltext, fontsize='xx-large')

#set ticks
ax = plt.gca()
ax.yaxis.set_ticks_position('left')
ax.get_yaxis().set_tick_params(direction='in', width=1)
plt.axvline(0.470933)
plt.axvline(0.970933)

plt.savefig("../graph/compare.png")
plt.show()
# for i in range(0,8):
#     datalist = []
#     for j in range(0,301):
#         print data[j][i]
#         datalist = np.append(datalist,data[j][i])
#     col[i] = datalist
#     print col[i]
# print data([1][2])
# for i in range(0,10):
#     # print i
#        data = np.array([])
#        for j in range(0,302):
#            line = fh.readline()
#            line = line.split()
#         # print line
#            print line
#         # print line[i]
#        data = np.append(data,line[i])
#     # print data
#   #  datalist = np.append(data,datalist)
#     # print datalist
