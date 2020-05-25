# -*- coding : utf - 8 -*-

import numpy as np
import matplotlib.pyplot as plt

class DLP:
    def sigmoid(self,x):
        return 1 / (1 + np.exp(-x)) #NL ftn으로 sigmoid를 정의하였다.

    def unit(self,x):  # 스칼라를 판단하는 거임.
        if x >= 0:
            return 1
        else:
            return 0
        
    def __init__(self):
        ##################게이트 이름(타입) 초기화####################
        self.name = input('어떠한 논리게이트를 설계하실 생각인가요? : ')  # XOR
        print(f'\n{self.name}를 설계합니다.')

        ###################트레이닝 데이터 초기화####################
        self.n = int(input('\n트레이닝 데이터를 몇개 넣을 생각이신가요? : '))  # 4
        tmp_x = [[1.0] for i in range(self.n)]  # 미리 bias를 위한 x0항을 반영하고, n개의 train_x를 맞이할 준비를 하였다.
        tmp_y = []
        for i in range(self.n):
            x_buffer = input(
                f'{i + 1}번쨰 트레이닝 데이터의 x_벡터 좌표값을 입력해주세요 (입력 예시 : (0,0이면) 0 0 ) : ').strip().split()  # 0 0 입력후 그 스트링을 리스트로 캐스트
            x_buffer = list(map(float, x_buffer))  # 리스트 각각의 원소를 str타입에서 float타입으로 캐스트
            tmp_x[i].extend(x_buffer)

            y_buffer = float(
                input(f'{i + 1}번쨰 트레이닝 데이터의 y벡터 좌표값을 입력해주세요 (입력 예시  : (0이면) 0 : ').strip())  # 0 입력후 그 스트링을 float으로 캐스
            tmp_y.append(y_buffer)

        self.train_x = np.array(tmp_x).reshape(self.n, -1)
        self.k = len(tmp_x[0])
        self.y = np.array(tmp_y)

        ###################시스템 벡터 초기화####################
        self.i = int(input('hidden layer의 노드의 갯수는? : '))
        #self.j = int(input('hidden layer의 노드 벡터의 갯수는? '))

        print('\n시스템 벡터들을 가우사안 분포를 택하여 랜덤하게 초기화시키려 합니다. 원하시는 평균과 표준분포를 입력하세요.')
        mean = float(input('평균 :').strip())
        vari = float(input('표준편차 :').strip())
        self.w_ij = np.random.normal(mean, vari, self.i).reshape(self.i, -1)  # ix1 행렬
        self.w_ki = np.random.normal(mean, vari, self.k * self.i).reshape(self.k, -1)  # kxi 행렬

        self.a_in = (self.train_x * self.w_ki).reshape(self.k,-1)

        ###################Learning Rate 초기화####################
        self.lr = float(input('\n원하시는 Learing Rate를 입력하세요 : ').strip())
        print(f'초기화된 값들은 다음과 같습니다\n\n name : {self.name}\ntrain_x : {self.train_x}\ny : {self.y}\nw_ij : {self.w_ij}\nw_ki : {self.w_ki}\nlr : {self.lr}')



class LogicGate:
    def __init__(self,name='',train_x_=[],y=[],w_=[],lr=0.5): #멤버 변수 : 논리게이트 이름,트레이닝 x들,라벨 y들,시스템 벡테 w_,learning rate인 lr

        ###################게이트 이름(타입) 초기화####################
        self.name = input('어떠한 논리게이트를 설계하실 생각인가요? : ') #AND
        print(f'\n{self.name}를 설계합니다.')

        ###################트레이닝 데이터 초기화####################
        self.n = int(input('\n트레이닝 데이터를 몇개 넣을 생각이신가요? : ')) #4
        tmp_x = [[1.0] for i in range(self.n)] # 미리 bias를 위한 x0항을 반영하고, n개의 train_x를 맞이할 준비를 하였다.
        tmp_y = []
        for i in range(self.n) :
            x_buffer = input(f'{i+1}번쨰 트레이닝 데이터의 x_벡터 좌표값을 입력해주세요 (입력 예시 : (0,0이면) 0 0 ) : ').strip().split() #0 0 입력후 그 스트링을 리스트로 캐스트
            x_buffer = list(map(float,x_buffer)) #리스트 각각의 원소를 str타입에서 float타입으로 캐스트
            tmp_x[i].extend(x_buffer)

            y_buffer = float(input(f'{i + 1}번쨰 트레이닝 데이터의 y벡터 좌표값을 입력해주세요 (입력 예시  : (0이면) 0 : ').strip())  # 0 입력후 그 스트링을 float으로 캐스
            tmp_y.append(y_buffer)

        self.train_x = np.array(tmp_x).reshape(self.n,-1)
        self.k = len(tmp_x[0])
        self.y = np.array(tmp_y)

        ###################시스템 벡터 초기화####################
        self.i = int(input('hidden layer의 노드의 갯수는? : '))
        self.j = int(input('hidden layer의 노드 벡터의 갯수는? '))

        print('\n시스템 벡터들을 가우사안 분포를 택하여 랜덤하게 초기화시키려 합니다. 원하시는 평균과 표준분포를 입력하세요.')
        mean = float(input('평균 :').strip())
        vari = float(input('표준편차 :').strip())
        self.w_ij = np.random.normal(mean,vari,self.i).reshape(self.i,-1) #ix1 행렬
        self.w_ki = np.random.normal(mean,vari,self.k * self.j).reshape(self.k,-1) #kxi 행렬

        ###################Learning Rate 초기화####################
        self.lr = float(input('\n원하시는 Learing Rate를 입력하세요 : ').strip())
        print(f'초기화된 값들은 다음과 같습니다\n\n name : {name}\ntrain_x : {train_x_}\ny : {y}\nw_ : {w_}\nlr : {lr}')

    def sigmoid(self,x):
        return 1 / (1 + np.exp(-x)) #NL ftn으로 sigmoid를 정의하였다.

    def unit(self,x):  # 스칼라를 판단하는 거임.
        if x >= 0:
            return 1
        else:
            return 0

    def slp_network(self):
        """proactivation """

        a_ = np.dot(self.train_x, self.w_)  # proactivation
        print(f'a_ : {a_}\n')

        """ y_estimate값 """

        y_ = np.array(list(map(self.sigmoid, a_)))  # y추정값
        print(f'y_ : {y_}\n')

        cost = (self.y - y_) ** 2

        print(f'y-y_ : {self.y - y_}\n')
        print(f'(y-y_)**2 : {(self.y - y_) ** 2}\n')
        print(f'cost : {sum((self.y - y_) ** 2)}\n')

        for i in range(20000):
            cost_gradient = []  # cost를 weight vector로 미분한 그래디언트 벡터의 마이너

            for k in range(self.k):  # w0 , w1 , w2 각각들에 대한 cost의 편미분값을 cost_gradient 리스트에 넣을 예
                tmp = 0

                for n in range(self.n):
                    tmp += -((self.train_x[n][k]) * (y_[n]) * (1 - y_[n]) * (self.y[n] - y_[n]))

                cost_gradient.append(tmp)

            cost_gradient = np.array(cost_gradient)
            # print(f'cost_gradient의 값 : {cost_gradient}')
            self.w_ = self.w_ - (self.lr) * cost_gradient
            # print(f'바뀐 w_ 의 값 : {w_}')
            a_ = np.dot(self.train_x, self.w_)
            y_ = np.array(list(map(self.sigmoid, a_)))
            cost = (self.y - y_) ** 2
            # print(f'cost : {sum((y - y_) ** 2)}\n')

        print(f'트레이닝 데이터로 {self.train_x}를 넣고 학습을 한 결과, w_는 {self.w_}로 최적화 되었고, 그로 인한 추정값 y_는 {y_}입니다.')

    def test_and_plot(self):
        test_data = []
        x1 = np.linspace(0, 2, 10)
        x2 = np.linspace(0, 2, 10)
        for i in range(10):
            for j in range(10):
                test_data.append([1, x1[i], x2[j]])

        z = list(map(self.unit, (np.dot(test_data, self.w_))))

        for i in range(len(z)):
            if z[i] == 1:
                plt.scatter(test_data[i][1], test_data[i][2], c='b')
            elif z[i] == 0:
                plt.scatter(test_data[i][1], test_data[i][2], c='y')
        plt.xlabel('x1')
        plt.ylabel('x2')
        plt.title('AND GATE (BLUE: True , YELLOW : False)')

        plt.show()
    def return_w_(self):
        return self.w_


#####main 함수#####

xor_gate = DLP()