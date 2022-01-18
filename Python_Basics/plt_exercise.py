#encoding: utf-8
'''
习题来源：
1. LintCode人工智能学习：https://www.lintcode.com/learn/
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


'''
创建plt

    <-- QUOTE：https://stackoverflow.com/questions/34162443/why-do-many-examples-use-fig-ax-plt-subplots-in-matplotlib-pyplot-python @jonchar -->
    plt.subplots() is a function that returns a tuple containing a figure and axes object(s). 
    Thus when using fig, ax = plt.subplots() you unpack this tuple into the variables fig and ax. 
    Having fig is useful if you want to change figure-level attributes or save the figure as an image file later (e.g. with fig.savefig('yourfilename.png')). 
    You certainly don't have to use the returned figure object but many people do use it later so it's common to see. 
    Also, all axes objects (the objects that have plotting methods), have a parent figure object anyway.

    fig: 文件层面
    ax: 图像信息层面

'''
plt.figure() 
plt.subplot(2,2,1)
fig, ax = plt.subplots(2,2)
# 上面两种return的值都不能unpack成两个
# 第一行的写法可以等价为 fig, ax = plt.subplots(1)


'''
plt 画图
参考: https://www.lintcode.com/learn/118/315
'''

# plt.plot() 默认点与点之间有顺序关系，可以连线，且可以分行表示不同的线段，marker_style可以写在一起
x1, y1, x2, y2 = np.arange(1, 10), np.arange(1, 10), np.arange(1, 20, 2), np.arange(1, 20, 2)*2
plt.figure()
plt.plot(
    x1, y1, 'ro--', # 'ro--为marker_style 表示为红色圆圈+横线'
    x2, y2, 'b*-.') 
plt.savefig('test1.jpg')

# plt.scatter() 默认点与点之间无顺序关系，无连线，必须用两个scatter画分别的线段，marker_style颜色和marker分开写
plt.figure()
plt.scatter(x1, y1, c = 'r', marker = 'o')
plt.scatter(x2, y2, c = 'b', marker = '*')
plt.savefig('test2.jpg')

