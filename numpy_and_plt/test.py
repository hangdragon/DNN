# -*- coding:utf-8 -*-
import numpy as np

def leaky_relu(ndarray_x):
    if len(ndarray_x.shape) == 0: #스칼라일때
        if ndarray_x>0 :
            return ndarray_x
        else :
            return 0.1 * ndarray_x
    else :
        positive = np.array(list(map(lambda x : x * (x>0),ndarray_x)))
        negative = np.array(list(map(lambda x: 0.1* x * (x <= 0), ndarray_x)))
        return positive + negative

def diff_leaky_relu(ndarray_x):
    if len(ndarray_x.shape) == 0:  # 스칼라일때
        if ndarray_x > 0:
            return 1
        else:
            return 0.01
    else:
        positive = np.array(list(map(lambda x: 1 * (x > 0), ndarray_x)))
        negative = np.array(list(map(lambda x: 0.1 * (x <= 0), ndarray_x)))
        return positive + negative
    #####################################
def leaky_relu(ndarray_x,coefficient = 0.01):
    if len(ndarray_x.shape) == 0:  # 스칼라일때
        if ndarray_x > 0:
            return ndarray_x
        else:
            return coefficient * ndarray_x

    elif len(ndarray_x.shape) == 1:  # 1차원 행렬일때
        result = [[] for i in range(len(ndarray_x))]
        for row in range(len(ndarray_x)):
            if ndarray_x[row] > 0:
                result[row] = ndarray_x[row]
            else:
                result[row] = coefficient * ndarray_x[row]

    elif len(ndarray_x.shape) == 2:  # 1차원 행렬일때
        result = [[] for i in range(len(ndarray_x))]
        for row in range(len(ndarray_x)):
            for column in range(len(ndarray_x[row])):
                if ndarray_x[row][column] > 0:
                    result[row].append(ndarray_x[row][column])
                else:
                    result[row].append(coefficient * ndarray_x[row][column])
    return np.array(result)

def diff_leaky_relu(ndarray_x,coefficient = 0.01):
    if len(ndarray_x.shape) == 0:  # 스칼라일때
        if ndarray_x > 0:
            return 1
        else:
            return coefficient

    elif len(ndarray_x.shape) == 1: # 1차원 행렬일때
        result = [[] for i in range(len(ndarray_x))]
        for row in range(len(ndarray_x)):
            if ndarray_x[row] > 0 :
                result[row] = 1
            else :
                result[row] = coefficient

    elif len(ndarray_x.shape) == 2: # 1차원 행렬일때
        result = [[] for i in range(len(ndarray_x))]
        for row in range(len(ndarray_x)):
            for column in range(len(ndarray_x[row])):
                if ndarray_x[row][column] > 0 :
                    result[row].append(1)
                else :
                    result[row].append(coefficient)
    return np.array(result)

def sigmoid(ndarray_x):
    return 1 / (1 + np.exp(-ndarray_x))  # NL ftn으로 sigmoid를 정의하였다.

def diff_sigmoid(ndarray_x):
    return sigmoid(ndarray_x)*(1-sigmoid(ndarray_x))

def unit(ndarray_x):  # ndarray_x 벡터의 원소들을 하나하나 unit함수에 집어넣는다.
    for i in range(len(ndarray_x)):
        if ndarray_x[i] >= 0:
            ndarray_x[i] = 1
        else:
            ndarray_x[i] = 0

def activation_ftn(ndarray,ftn):
    if ftn == sigmoid :
        return ftn(ndarray)
    elif ftn == leaky_relu :
        return leaky_relu(ndarray)
    elif ftn == diff_leaky_relu :
        return diff_leaky_relu(ndarray)
    elif ftn == diff_sigmoid :
        return diff_sigmoid(ndarray)

def select_ftn():
    pass
#select_ftn = input('Activation ftn으로 어떤걸 선택하시겠습니까? ')

print(activation_ftn(np.arange(-5,5).reshape(5,-1),leaky_relu))
print()
print(activation_ftn(np.arange(-5,5).reshape(5,-1),diff_leaky_relu))
print()
print(activation_ftn(np.arange(-5,5).reshape(5,-1),sigmoid))
print()
print((activation_ftn(np.arange(-5,5).reshape(5,-1),diff_sigmoid))*10)