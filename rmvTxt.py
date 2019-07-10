# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:31:55 2019

@author: Administrator
"""

import os
n = 0
for root, dirs, files in os.walk("/home/riley/Documents/fromGit/Dissertation-2019/trainingdata_backup"):
    for name in files:
        if(name.endswith(".txt")):
            n += 1
            os.remove(os.path.join(root, name))
print(n)