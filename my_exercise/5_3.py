# -*- coding:utf-8 -*-

# dict에서 모든 key들을 불러와서 리스트에 저장하는 방법 : list_tmp = [i for i in dict_a.keys()]

import numpy as np

def operation(ftn):
    return ftn()

def add(list1=[1,2,3,4],list2=[3,4,5,6]) :
    return np.add(list1,list2)

list1 = [1,2,3,4]

list2 = [3,4,5,6]

print(operation(add))