# -*- coding : utf - 8 -*-

import numpy as np
import matplotlib.pyplot as plt

class DLP :

    def relu(self,ndarray_x):
        result = [[] for i in range(len(ndarray_x))]
        for row in range(len(ndarray_x)):
            for column in range(len(ndarray_x[row])):
                if ndarray_x[row][column] >= 0:
                    result[row].append(ndarray_x[row][column])
                else:
                    result[row].append(0)
        return np.array(result)

    def diff_relu(self,ndarray_x):
        result = [[] for i in range(len(ndarray_x))]
        for row in range(len(ndarray_x)):
            for column in range(len(ndarray_x[row])):
                if ndarray_x[row][column] >= 0:
                    result[row].append(1)
                else:
                    result[row].append(0)
        return np.array(result)

    def sigmoid(self,ndarray_x):
        return 1 / (1 + np.exp(-ndarray_x)) #NL ftn으로 sigmoid를 정의하였다.

    def unit(self,ndarray_x):  # ndarray_x 벡터의 원소들을 하나하나 unit함수에 집어넣는다.
        for i in range(len(ndarray_x)) :
            if ndarray_x[i] >= 0:
                ndarray_x[i] = 1
            else:
                ndarray_x[i] = 0

    def __init__(self): #생성자는 아키텍처를 선택하고, 웨이트들을 이니셜라이즈 해준다.
        ########## layer의 갯수(layer_number)입력 ###########
        self.layer_number = int(input('원하시는 레이어의 갯수를 입력하세요(1이상인 정수입니다!) : '))
        if self.layer_number == 1 :
            print('{}를 선택하셨습니다.'.format('SLP'))
        elif self.layer_number == 1 :
            print('{}를 선택하셨습니다.'.format('DLP'))
        else :
            print('{}를 선택하셨습니다.'.format('MLP'))

        ########## 자료의 갯수들(k,i,j,n....)입력 ############
        self.n = int(input('\n원하시는 트레이닝 데이터의 갯수를 입력하세요 : ')) #ex) (0,0),(0,1),(1,0),(1,1)이면 n = 4
        self.k = int(input('원하시는 트레이닝 데이터의 길이를 입력하세요 : ')) #ex) 각 트레이닝 데이터가 길이가 2인 1차원 벡터이므로 k = 2
        self.i = int(input('원하시는 히든레이어 노드 갯수를 입력하세요 : '))  # ex) 3
        self.j = int(input('원하시는 출력의 갯수를 입력하세요 : ')) #ex) (0,0)과 (0,1)은 (1,2)로 , (1,0)과 (1,1)은 (3,4)로 가게 하고싶다면 출력벡터가 길이가 2인 1차원 벡터이므로 n = 2

        ########## 트레이닝 데이터들 (x벡터들) 입력 ############
        print('\n트레이닝 데이터를 하나씩 입력하세요. (입력 예시 : (0,0)이면 >>>0 0)\n')
        self.x_ = np.zeros((self.n,(self.k)+1)) #nxk행렬인 트레이닝 데이터의 틀을 만들었음.
        for i in range(self.n) :
            self.x_[i][0] = 1 #각 행들의 첫항에 bias를 위한 항인 1을 초기화.
            self.x_[i][1:] = list(map(float,input(f'길이가 {self.k}인 {(i + 1)}번째 트레이닝 데이터 입력 >>').strip().split()))

        ########## 레이블들 (y벡터들) 입력 ############
        print('\n라벨들을 하나씩 입력하세요. (입력 예시 : (1,2)이면 >>>1 2)\n')
        self.y_ = np.zeros((self.n, self.j))  # nxj행렬인 트레이닝 데이터의 틀을 만들었음.
        for j in range(self.n):
            self.y_[j] = list(map(float, input(f'길이가 {self.j}인 {(j + 1)}번째 레이블 입력 >>').strip().split()))

        ########## 웨이트벡터들 (w벡터들) 초기화 ############
        print('#######1번째 layer의 weight 초기화#######') #wki는 kxi짜리 행렬
        print(f'\n입력이 길이가 {self.k} , 히든레이어 노드갯수가 {self.i}개인 SLP에서의 파라미터의 갯수는 {((self.k)+1) * self.i}개 입니다. ex) wki...') #bias 항까지 포함해서 self.k + 1을 해줬음.
        print(f'{1}번째 레이어의 웨이트 벡터들을 가우시안 분포로 초기화 하겠습니다.\n원하시는 평균과 분산을 입력하세요')
        muy = float(input('평균 : '))
        sigma = float(input('표준편차 : '))
        self.w_ki = np.random.normal(muy, sigma, (((self.k)+1),self.i)) #1번째 layer의 웨이트 벡터들

        print('#######2번째 layer의 weight 초기화#######') #wij는 ixj짜리 행렬
        print(f'\n히든레이어 노드 갯수가 {self.i} ,출력 노드 갯수가 {self.j}개인 SLP에서의 파라미터의 갯수는 {self.i* self.j}개 입니다. ex) wij...')  # bias 항까지 포함해서 self.k + 1을 해줬음.
        print(f'{2}번째 레이어의 웨이트 벡터들을 가우시안 분포로 초기화 하겠습니다.\n원하시는 평균과 분산을 입력하세요')
        muy = float(input('평균 : '))
        sigma = float(input('표준편차 : '))
        self.w_ij = np.random.normal(muy, sigma, (self.i, self.j))  # 1번째 layer의 웨이트 벡터들

        ########## 나머지 a_와 y_들 ##########
        self.ha1_ = []
        self.hy1_est = []  # 히든레이어 1의 y값들

        self.a_ = []
        self.y_est = []

        self.cost = 0

        ###########learning rate 입력############
        self.lr = float(input('\n원하시는 learning rate를 입력해주세요 : '))

    def feed_forward(self):
        self.ha1_ = np.dot(self.x_, self.w_ki) ########## proactivation들 (a벡터들) 초기화 ############
        self.hy1_est = self.sigmoid(self.ha1_)  ########## y_est들 (y추정값 벡터들) 초기화 ############

        self.a_ = np.dot(self.hy1_est, self.w_ij)  ########## proactivation들 (a벡터들) 초기화 ############
        self.y_est = self.sigmoid(self.a_) ########## y_est들 (y추정값 벡터들) 초기화 ############

        self.cost = sum(self.y_ - self.y_est)**2 ########## cost 초기화 ############
        print(f'a_는 {self.a_}\ny_est는 {self.y_est}\ncost는 {self.cost}')

    def gradient_back_propagation(self,loop_number = 60000):
        delta_j_ = np.zeros((self.n, self.j))  # nxj행렬인 트레이닝 데이터의 틀을 만들었음.
        delta_i_ = np.zeros((self.n, self.i))  # nxi행렬인 트레이닝 데이터의 틀을 만들었음.

        for update in range(loop_number) :
            for j in range(self.j):
                for i in range(self.i):
                    gradient = 0
                    for n in range(self.n):
                        delta_j_[n][j] = (self.y_[n][j] - self.y_est[n][j]) * self.y_est[n][j] * (1 - self.y_est[n][j])
                        gradient += -(self.hy1_est[n][i]) * delta_j_[n][j]
                    # n번 루프 다 돌았고,
                    self.w_ij[i][j] = self.w_ij[i][j] - ((self.lr) * gradient)

            for i in range(self.i):
                for k in range((self.k)+1):
                    gradient = 0
                    for n in range(self.n) :
                        for j in range(self.j):
                            tmp = 0
                            tmp += (self.w_ij[i][j])*delta_j_[n][j]
                        delta_i =  self.hy1_est[n][i] * (1 - self.hy1_est[n][i]) * tmp
                        gradient += -(self.x_[n][k])*delta_i
                    #n번 루프 다 돌았고,
                    self.w_ki[k][i] = self.w_ki[k][i] -((self.lr)*gradient)

            self.ha1_ = np.dot(self.x_, self.w_ki)  ########## proactivation들 (a벡터들) 초기화 ############
            self.hy1_est = self.sigmoid(self.ha1_)  ########## y_est들 (y추정값 벡터들) 초기화 ############

            self.a_ = np.dot(self.hy1_est, self.w_ij)  ########## proactivation들 (a벡터들) 초기화 ############
            self.y_est = self.sigmoid(self.a_)  ########## y_est들 (y추정값 벡터들) 초기화 ############

            self.cost = sum((self.y_ - self.y_est)**2)  ########## cost 초기화 ############

            #print(f'a_는 {self.a_}\ny_est는 {self.y_est}\ncost는 {self.cost}')

            #print(f'업데이트된 cost는 {self.cost}')
            #print(f'w_ki = {self.w_ki}')



    def show(self):
        print(f'x_ = {self.x_}\n')
        print(f'y_ = {self.y_}\n')
        print(f'y_est = {self.y_est.round()}\n')
        print(f'w_ki = {self.w_ki}\n')
        print(f'cost = {self.cost}\n')

slp =DLP()
slp.feed_forward()
slp.gradient_back_propagation()
slp.show()

