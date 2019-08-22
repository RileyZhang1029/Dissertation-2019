# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import fmin
#X轴，Y轴数据
x = [1,2,4,8,16,32]
y = [0.324, 0.353, 0.357, 0.360, 0.365, 0.356]
plt.figure(figsize=(8,5)) #创建绘图对象
plt.title('Accuracy at Different Batch Sizes')

plt.ylim(0.32,0.37)
plt.xlim(0, 33)
plt.xticks(x)
plt.plot(x,y,color = 'black',linewidth = 1.2, linestyle = '-.',marker='o', ms=3)   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
plt.xlabel("Batch Size") #X轴标签
plt.ylabel("Accuracy")  #Y轴标签
#plt.title("Line plot") #图标题
plt.grid(axis='y')
 #设置数字标签**
for a,b in zip(x,y):
    plt.text(a, b, '%.3f' % b, ha='center', va= 'bottom',fontsize=10)
plt.savefig("/home/riley/Pictures/batchsize.png") #保存图
plt.show()  #显示图


#dropput rate
x = [0.1,0.2,0.3,0.4,0.5]
y = [0.356, 0.365, 0.323, 0.362, 0.194]
plt.figure(figsize=(8,5)) #创建绘图对象
plt.title('Accuracy at Different Dropout Rates')
plt.ylim(0.18,0.375)
plt.xlim(0.0, 0.6)
plt.xticks(x)
plt.plot(x,y,color = 'black',linewidth = 1.2, linestyle = '-.',marker='o', ms=3)   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
plt.xlabel("Dropout Rate") #X轴标签
plt.ylabel("Accuracy")  #Y轴标签
#plt.title("Line plot") #图标题
plt.grid(axis='y')
 #设置数字标签**
for a,b in zip(x,y):
    plt.text(a, b, '%.3f' % b, ha='center', va= 'bottom',fontsize=10)
plt.savefig("/home/riley/Pictures/dropout.png") #保存图
plt.show()  #显示图

#trainingcurve
x = np.array([0.25,0.5,0.75,1.0])
y = np.array([0.20, 0.27, 0.32, 0.36])


plt.figure(figsize=(8,5)) #创建绘图对象

plt.ylim(0.18,0.375)
plt.xlim(0.2, 1.05)
plt.title('Accuracy at Different Proportions of Training Examples')
plt.xticks(x)
plt.grid(axis='y')
#插值法之后的x轴值，表示从0到10间距为0.5的200个数
xnew =np.arange(-1,1.2,0.02)#实现函数
func = interp1d(x,y,kind='cubic',bounds_error=False)
# #利用xnew和func函数生成ynew,xnew数量等于ynew数量
ynew = func(xnew)

# 原始折线
plt.plot(x, y, color = 'black', linewidth = 1.2, linestyle = '-.' ,marker='o', ms=3)
#平滑处理后曲线
# plt.plot(xnew,ynew)

plt.xlabel("Proportion of Training Data") #X轴标签
plt.ylabel("Accuracy")  #Y轴标签

#  #设置数字标签**
for a,b in zip(x,y):
    plt.text(a, b, '%.3f' % b, ha='center', va= 'bottom',fontsize=10)
plt.savefig("/home/riley/Pictures/curve.png") #保存图
plt.show()  #显示图





# plt.plot(x,y,color = 'black',linewidth = 1.2)   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）




