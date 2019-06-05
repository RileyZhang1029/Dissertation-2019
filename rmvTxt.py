# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:31:55 2019

@author: Administrator
"""

import os
n = 0
for root, dirs, files in os.walk("C:/Users/Administrator/Documents/GitHub/Dissertation-2019/trainingdata"):
    for name in files:
        if(name.endswith(".txt")):
            n += 1
            print(n)
            os.remove(os.path.join(root, name))