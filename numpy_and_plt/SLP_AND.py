# -*- coding : utf - 8 -*-

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
def unit(a) : #스칼라를 판단하는 거임.
    if a >= 0 :
        return 1
    else :
        return 0

def sigmoid(x) :
    return 1/(1+np.exp(-x))

def relu(x) :
    if x>=0 :
        return x
    else :
        return 0

def leaky_relu(x) :
    if x>=0 :
        return x
    else :
        return 0.1*x

lr = 0.5
"""" traing data & labeling """

label_dict = {
    (1,0,0) : 0, #(x0,x1,x2) = (1,0,0) -> y = 0
    (1,1,0) : 0, #(x0,x1,x2) = (1,0,1) -> y = 0
    (1,0,1) : 0, #(x0,x1,x2) = (1,1,0) -> y = 0
    (1,1,1) : 1  #(x0,x1,x2) = (1,1,1) -> y = 1
} #key값이 training data이고, value값이 label이다. x_에서 x0는 bias를 위한 값이다.

y = np.array(tuple([label_dict[i] for i in label_dict]))#Ground Truth Value
print(f'y : {y}\n')
"""weight vector and bias """

w_ = np.random.normal(0,1,3) #weight vector 초기화
print(f'w_ : {w_}\n')

"""proactivation """

a_ = [np.dot(i,w_) for i in label_dict] #proactivation
print(f'a_ : {a_}\n')

""" y_estimate값 """

y_ = np.array(list(map(sigmoid,a_))) #y추정값
print(f'y_ : {y_}\n')


cost = (y-y_)**2

print(f'y-y_ : {y-y_}\n')
print(f'(y-y_)**2 : {(y-y_)**2}\n')
print(f'cost : {sum((y-y_)**2)}\n')


for i in range(20000) :
    cost_gradient = []  # cost를 weight vector로 미분한 그래디언트 벡터의 마이너

    for k in range(3):  # w0 , w1 , w2 각각들에 대한 cost의 편미분값을 cost_gradient 리스트에 넣을 예
        tmp = 0
        i = 0
        for j in label_dict:
            tmp += -((j[k]) * (y_[i]) * (1 - y_[i]) * (label_dict[j] - y_[i]))
            i += 1
        cost_gradient.append(tmp)

    cost_gradient = np.array(cost_gradient)
    #print(f'cost_gradient의 값 : {cost_gradient}')
    w_ = w_ -(lr)*cost_gradient
    #print(f'바뀐 w_ 의 값 : {w_}')
    a_ = [np.dot(i, w_) for i in label_dict]
    y_ = np.array(list(map(sigmoid, a_)))
    cost = (y - y_) ** 2
    #print(f'cost : {sum((y - y_) ** 2)}\n')

print(f'\nw_은 {w_} 이고, y_은 {y_}이다. ')

training_data = []
x1 = np.linspace(0,2,10)
x2 = np.linspace(0,2,10)
for i in range(10) :
    for j in range(10):
        training_data.append([1,x1[i],x2[j]])

z = list(map(unit,(np.dot(training_data,w_))))
print(*z)
for i in range(len(z)):
    if z[i] == 1:
        plt.scatter(training_data[i][1], training_data[i][2], c='b')
    elif z[i] == 0 :
        plt.scatter(training_data[i][1], training_data[i][2], c='y')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('AND GATE (BLUE: True , YELLOW : False)')

plt.show()

