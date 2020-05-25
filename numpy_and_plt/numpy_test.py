# -*- coding: utf-8 -*-

#ndarray가지고 for문을 돌려볼꺼야

import numpy as np

loop = np.arange(10).reshape(5,-1) # loop = 2차원 ndarray가 들어갔는데, [[0,1] [2,3]]//
for i in loop : #행이 걸리는거고
    for j in i: # 열이 걸리는거고
        print(j)