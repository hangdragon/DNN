# -*- coding : utf - 8 -*-

import numpy as np
import matplotlib.pyplot as plt


class SLP_ki:

    def relu(self, ndarray_x):
        result = [[] for i in range(len(ndarray_x))]
        for row in range(len(ndarray_x)):
            for column in range(len(ndarray_x[row])):
                if ndarray_x[row][column] >= 0:
                    result[row].append(ndarray_x[row][column])
                else:
                    result[row].append(0)
        return np.array(result)

    def diff_relu(self, ndarray_x):
        result = [[] for i in range(len(ndarray_x))]
        for row in range(len(ndarray_x)):
            for column in range(len(ndarray_x[row])):
                if ndarray_x[row][column] >= 0:
                    result[row].append(1)
                else:
                    result[row].append(0)
        return np.array(result)

    def sigmoid(self, ndarray_x):
        return 1 / (1 + np.exp(-ndarray_x))  # NL ftn으로 sigmoid를 정의하였다.

    def unit(self, ndarray_x):  # ndarray_x 벡터의 원소들을 하나하나 unit함수에 집어넣는다.
        for i in range(len(ndarray_x)):
            if ndarray_x[i] >= 0:
                ndarray_x[i] = 1
            else:
                ndarray_x[i] = 0

    def __init__(self, lr=0.5):  # 생성자는 아키텍처를 선택하고, 웨이트들을 이니셜라이즈 해준다. lr를 미리 설정해준다.
        ########## layer의 갯수(layer_number)입력 ###########
        self.layer_number = int(input('원하시는 레이어의 갯수를 입력하세요(1이상인 정수입니다!) : '))
        if self.layer_number == 1:
            print('{}를 선택하셨습니다.'.format('SLP'))
        elif self.layer_number == 1:
            print('{}를 선택하셨습니다.'.format('DLP'))
        else:
            print('{}를 선택하셨습니다.'.format('MLP'))

        ########## 자료의 갯수들(k,i,j,n....)입력 ############
        self.n = int(input('\n원하시는 트레이닝 데이터의 갯수를 입력하세요 : '))  # ex) (0,0),(0,1),(1,0),(1,1)이면 n = 4
        self.k = int(input('원하시는 트레이닝 데이터의 길이를 입력하세요 : '))  # ex) 각 트레이닝 데이터가 길이가 2인 1차원 벡터이므로 k = 2
        self.i = int(input(
            '원하시는 출력의 갯수를 입력하세요 : '))  # ex) (0,0)과 (0,1)은 (1,2)로 , (1,0)과 (1,1)은 (3,4)로 가게 하고싶다면 출력벡터가 길이가 2인 1차원 벡터이므로 n = 2

        ########## 트레이닝 데이터들 (x벡터들) 입력 ############
        print('\n트레이닝 데이터를 하나씩 입력하세요. (입력 예시 : (0,0)이면 >>>0 0)\n')
        self.x_ = np.zeros((self.n, (self.k) + 1))  # nxk행렬인 트레이닝 데이터의 틀을 만들었음.
        for i in range(self.n):
            self.x_[i][0] = 1  # 각 행들의 첫항에 bias를 위한 항인 1을 초기화.
            self.x_[i][1:] = list(map(float, input(f'길이가 {self.k}인 {(i + 1)}번째 트레이닝 데이터 입력 >>').strip().split()))

        ########## 레이블들 (y벡터들) 입력 ############
        print('\n라벨들을 하나씩 입력하세요. (입력 예시 : (1,2)이면 >>>1 2)\n')
        self.y_ = np.zeros((self.n, self.i))  # nxi행렬인 트레이닝 데이터의 틀을 만들었음.
        for i in range(self.n):
            self.y_[i] = list(map(float, input(f'길이가 {self.i}인 {(i + 1)}번째 레이블 입력 >>').strip().split()))

        ########## 웨이트벡터들 (w벡터들) 초기화 ############
        print(
            f'\n입력이 길이가 {self.k} , 출력이 {self.i}개인 SLP에서의 파라미터의 갯수는 {((self.k) + 1) * self.i}개 입니다. ex) wki...')  # bias 항까지 포함해서 self.k + 1을 해줬음.
        print(f'{1}번째 레이어의 웨이트 벡터들을 가우시안 분포로 초기화 하겠습니다.\n원하시는 평균과 분산을 입력하세요')
        muy = float(input('평균 : '))
        sigma = float(input('표준편차 : '))
        self.w_ki = np.random.normal(muy, sigma, (((self.k) + 1), self.i))  # 1번째 layer의 웨이트 벡터들

        self.a_ = []
        self.y_est = []
        self.diff_y_est = []
        self.cost = 0

        ###########learning rate 입력############
        self.lr = lr

    def feed_forward(self):
        self.a_ = np.dot(self.x_, self.w_ki)  ########## proactivation들 (a벡터들) 초기화 ############
        self.y_est = self.relu(self.a_)  ########## y_est들 (y추정값 벡터들) 초기화 ############
        self.cost = sum(self.y_ - self.y_est) ** 2  ########## cost 초기화 ############
        self.diff_y_est = self.diff_relu(self.a_)
        print(f'a_는 {self.a_}\ny_est는 {self.y_est}\ncost는 {self.cost}\ndiff_y_est는 {self.diff_y_est}')

    def gradient_back_propagation(self, loop_number=20000):
        for update in range(loop_number):
            for i in range(self.i):
                for k in range((self.k) + 1):
                    gradient = 0
                    for n in range(self.n):
                        delta_i = (self.y_[n][i] - self.y_est[n][i]) * self.diff_y_est[n][i]
                        gradient += -(self.x_[n][k]) * delta_i
                    # n번 루프 다 돌았고,
                    self.w_ki[k][i] = self.w_ki[k][i] - ((self.lr) * gradient)

            self.a_ = np.dot(self.x_, self.w_ki)  ########## proactivation들 (a벡터들) 초기화 ############
            self.y_est = self.relu(self.a_)  ########## y_est들 (y추정값 벡터들) 초기화 ############
            self.diff_y_est = self.diff_relu(self.a_)
            self.cost = sum(self.y_ - self.y_est) ** 2  ########## cost 초기화 ############

            # print(f'업데이트된 cost는 {self.cost}')
            # print(f'w_ki = {self.w_ki}')

    def show(self):
        print(f'x_ = {self.x_}\n')
        print(f'y_ = {self.y_}\n')
        print(f'y_est = {self.y_est.round()}\n')
        print(f'w_ki = {self.w_ki}\n')
        print(f'cost = {self.cost}\n')


slp = SLP_ki(0.01)
slp.feed_forward()
slp.gradient_back_propagation()
slp.show()

