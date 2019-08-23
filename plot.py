# -*- coding: utf-8 -*-
"""
B134977
draw line charts in the dissertation
link to the Github Repostory: https://github.com/RileyZhang1029/Dissertation-2019
"""

import numpy as np
import matplotlib.pyplot as plt



#batch size
x = [1,2,4,8,16,32]
y = [0.324, 0.353, 0.357, 0.360, 0.365, 0.356]
plt.figure(figsize=(8,5)) #创建绘图对象
plt.title('Accuracy at Different Batch Sizes')

plt.ylim(0.32,0.37)
plt.xlim(0, 33)
plt.xticks(x)
plt.plot(x,y,color = 'black',linewidth = 1.2, linestyle = '-.',marker='o', ms=3)
plt.xlabel("Batch Size")
plt.ylabel("Accuracy")
#plt.title("Line plot")
plt.grid(axis='y')

for a,b in zip(x,y):
    plt.text(a, b, '%.3f' % b, ha='center', va= 'bottom',fontsize=10)
plt.savefig("/home/riley/Pictures/batchsize.png")
plt.show()


#dropput rate
x = [0.1,0.2,0.3,0.4,0.5]
y = [0.356, 0.365, 0.323, 0.362, 0.194]
plt.figure(figsize=(8,5)) #创建绘图对象
plt.title('Accuracy at Different Dropout Rates')
plt.ylim(0.18,0.375)
plt.xlim(0.0, 0.6)
plt.xticks(x)
plt.plot(x,y,color = 'black',linewidth = 1.2, linestyle = '-.',marker='o', ms=3) ）
plt.xlabel("Dropout Rate")
plt.ylabel("Accuracy")
#plt.title("Line plot")
plt.grid(axis='y')
for a,b in zip(x,y):
    plt.text(a, b, '%.3f' % b, ha='center', va= 'bottom',fontsize=10)
plt.savefig("/home/riley/Pictures/dropout.png") #保存图
plt.show()



#trainingcurve
x = np.array([0.25,0.5,0.75,1.0])
y = np.array([0.20, 0.27, 0.32, 0.36])
plt.figure(figsize=(8,5))
plt.ylim(0.18,0.375)
plt.xlim(0.2, 1.05)
plt.title('Accuracy at Different Proportions of Training Examples')
plt.xticks(x)
plt.grid(axis='y')
plt.plot(x, y, color = 'black', linewidth = 1.2, linestyle = '-.' ,marker='o', ms=3)
plt.xlabel("Proportion of Training Data")
plt.ylabel("Accuracy")
for a,b in zip(x,y):
    plt.text(a, b, '%.3f' % b, ha='center', va= 'bottom',fontsize=10)
plt.savefig("/home/riley/Pictures/curve.png")
plt.show()





