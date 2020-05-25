# -*- coding : utf - 8 -*-

import numpy as np
import matplotlib.pyplot as plt

class Perceptron :

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

    def architecture(self):
        ########## layer의 갯수(layer_number)입력 ###########
        self.number_of_layers = int(input('원하시는 레이어의 갯수를 입력하세요(1이상인 정수입니다!) : '))
        self.number_of_nodes = [[] for i in range(self.number_of_layers + 1)]  # SLP이면 x,y , DLP이면 x,h1,y,,,의 노드 갯수를 담으려고 만든 리스트.
        # x,h1,y에서 x는 트레이닝 데이터의 노드들 갯수. h1는 hidden layer1에 대한 노드들 갯수. y는 출력 데이터 노드들 갯수를 의미한다.
        #number_of_nodes라는 리스트 안에는 각 단계별 노드 갯수인 '스칼라'값이 들어간다. number_of_nodes의 길이는 number_of_layers의 +1!

        ##########  히든 레이어 갯수 및 입력,출력,히든 레이어 각각의 노드 갯수들 초기화 ############
        if self.number_of_layers == 1:
            print('{}를 선택하셨습니다.\n트레이닝 데이터, 출력 데이터 노드의 갯수를 각각 입력하세요.'.format('SLP'))
            for i in range(len(self.number_of_nodes)):
                if i == 0 :
                    self.number_of_nodes[i] = int(input('$트레이닝 데이터 노드 갯수(바이어스 항을 포함하여 +1 해주세요) >>>'))
                elif i == self.number_of_layers :
                    self.number_of_nodes[i] = int(input('$출력 데이터 노드 갯수 >>>'))

        elif self.number_of_layers == 2:
            print('{}를 선택하셨습니다.\n트레이닝 데이터, 히든 레이어 노드, 출력 데이터 노드의 갯수를 각각 입력하세요.'.format('DLP'))
            for i in range(len(self.number_of_nodes)):
                if i == 0 :
                    self.number_of_nodes[i] = int(input('$트레이닝 데이터 노드 갯수(바이어스 항을 포함하여 +1 해주세요) >>>'))
                elif i == self.number_of_layers :
                    self.number_of_nodes[i] = int(input('$출력 데이터 노드 갯수 >>>'))
                else :
                    self.number_of_nodes[i] = int(input('$히든 레이어 노드 갯수 >>>'))

        else:
            print('히든 레이어가 {}개인 {}를 선택하셨습니다.'.format(self.number_of_layers-1,'MLP'))
            print('\n트레이닝 데이터, 히든 레이어들의 노드, 출력 데이터 노드의 갯수를 각각 입력하세요.')
            for i in range(len(self.number_of_nodes)):
                if i == 0:
                    self.number_of_nodes[i] = int(input('$트레이닝 데이터 노드 갯수(바이어스 항을 포함하여 +1 해주세요) >>>'))
                elif i == self.number_of_layers:
                    self.number_of_nodes[i] = int(input('$출력 데이터 노드 갯수 >>>'))
                else:
                    self.number_of_nodes[i] = int(input(f'$히든 레이어{i}의 노드 갯수 >>>'))
            print(f'\n노드 갯수들은 다음과 같습니다 {self.number_of_nodes}')

        ############트레이닝 데이터의 갯수 입력#############
        self.number_of_training_data = int(input('\n원하시는 트레이닝 데이터의 갯수를 입력하세요 : '))  # ex) (0,0),(0,1),(1,0),(1,1)이면 n = 4

    def __init__(self): #생성자는 멤버 변수들의 선언 및 아키텍처 단계를 수행한다.

        self.number_of_layers = 0 # layer 갯수
        self.number_of_nodes = []  # 선택한 아키텍처에 대한 레이어별 노드 갯수들
        self.number_of_training_data = 0  # training data 갯수이자 label 갯수
        self.architecture() #architecture 멤버 함수를 실행하여 위의 세개의 변수 값을 초기화!

        self.number_of_input_node = self.number_of_nodes[0]
        self.number_of_output_node = self.number_of_nodes[-1]
        self.x_ = np.zeros((self.number_of_training_data,self.number_of_input_node)) #입력 트레이닝 데이터
        self.y_ = np.zeros((self.number_of_training_data, self.number_of_output_node))  #출력 트레이닝 데이터(레이블들)

        self.weight_for_layers = [[] for i in range(self.number_of_layers)] #전체 레이어의 갯수만큼 각각에 해당하는 웨이트 벡터들을 담을 리스트
        self.proactivation_for_layers = [[] for i in range(self.number_of_layers)]  # 전체 레이어의 갯수만큼 각각에 해당하는 proactivation 벡터들을 담을 리스트
        self.y_est_for_layers = [[] for i in range(self.number_of_layers)]  # 전체 레이어의 갯수만큼 각각에 해당하는 y 벡터들을 담을 리스트

        self.a_final = []
        self.y_est_final = []
        self.cost = 0 #최종 에러함수(비용함수)

        ###########learning rate 입력############
        self.lr = float(input('\n원하시는 learning rate를 입력해주세요 : '))

    def initialize(self):
        ########## 트레이닝 데이터들 (x벡터들) 입력 ############
        print('\n트레이닝 데이터를 하나씩 입력하세요. (입력 예시 : (0,0)이면 >>>0 0)\n')
        self.x_ = np.zeros((self.number_of_training_data, self.number_of_input_node))  # 트레이닝 데이터의 틀을 만들었음.
        for i in range(self.number_of_training_data):
            self.x_[i][0] = 1  # 각 행들의 첫항에 bias를 위한 항인 1을 초기화.
            self.x_[i][1:] = list(map(float, input(f'요소의 갯수가 {self.number_of_input_node-1}개인 {(i + 1)}번째 트레이닝 데이터 입력 >>').strip().split()))

        ########## 레이블들 (y벡터들) 입력 ############
        print('\n라벨들을 하나씩 입력하세요. (입력 예시 : (1,2)이면 >>>1 2)\n')
        self.y_ = np.zeros((self.number_of_training_data, self.number_of_output_node))  # 레이블의 틀을 만들었음.
        for j in range(self.number_of_training_data):
            self.y_[j] = list(map(float, input(f'요소의 갯수가 {self.number_of_output_node}인 {(j + 1)}번째 레이블 입력 >>').strip().split()))

        ########## 웨이트벡터들 (w벡터들) 초기화 ############
        for iter in range(len(self.weight_for_layers)) :
            print('#######{}번째 layer의 weight 초기화#######'.format(iter+1))  # 각 뉴런마다의 웨이트벡터를 초기화 해주기 위함
            print(f'\n제 {iter+1}번째 뉴런의 웨이트 벡터의 요소의 갯수는 {self.number_of_nodes[iter] * self.number_of_nodes[iter+1]}개 입니다.')
            print(f'{iter+1}번째 뉴런의 웨이트 벡터들을 가우시안 분포로 초기화 하겠습니다.\n원하시는 평균과 분산을 입력하세요')
            muy = float(input('평균 : '))
            sigma = float(input('표준편차 : '))
            self.weight_for_layers[iter] = np.random.normal(muy, sigma, (self.number_of_nodes[iter], self.number_of_nodes[iter+1]))  # 각 뉴런별로 웨이트 벡터를 가우시안으로 초기화

    def feed_forward_and_gradient_back_propagation(self,loop_number=30000):

        ########## 뉴런 갯수만큼 루프 돌면서 웨이트, proactivation, y추정값 전부 초기화 ##########

        for iter in range(self.number_of_layers): #뉴런 갯수만큼 루프 돌면서 웨이트, proactivation, y추정값 전부 초기화
            if iter == 0: #첫번째 뉴런의 proactivation, y추정값
                self.proactivation_for_layers[iter] = np.dot(self.x_, self.weight_for_layers[iter])  ########## 첫번째 proactivation (a벡터) 초기화 ############
                self.y_est_for_layers[iter] = self.sigmoid(self.proactivation_for_layers[iter])  ########## 첫번째 y_est (y추정값 벡터) 초기화 ############
            elif iter == self.number_of_layers-1: #마지막 뉴런의 proactivation, y추정값
                self.a_final = np.dot(self.y_est_for_layers[self.number_of_layers-2], self.weight_for_layers[self.number_of_layers-1])  ########## 마지막 proactivation (a벡터) 초기화 ############
                self.y_est_final = self.sigmoid(self.a_final)  ########## 마지막 y_est (y추정값 벡터) 초기화 ############

                self.proactivation_for_layers[iter] = np.dot(self.y_est_for_layers[iter - 1],self.weight_for_layers[iter])
                self.y_est_for_layers[iter] = self.sigmoid(self.proactivation_for_layers[iter])
            else : #각 뉴런의 proactivation, y추정값
                self.proactivation_for_layers[iter] = np.dot(self.y_est_for_layers[iter-1], self.weight_for_layers[iter])  ########## 첫번째 proactivation (a벡터) 초기화 ############
                self.y_est_for_layers[iter] = self.sigmoid(self.proactivation_for_layers[iter])  ########## 첫번째 y_est (y추정값 벡터) 초기화 ############

        self.cost = sum(self.y_ - self.y_est_final) ** 2  ########## cost 초기화 ############
        print(f'a_final는 {self.a_final}\ny_est_final는 {self.y_est_final}\ncost는 {self.cost}')

        ########## 각 뉴런에 해당하는 델타값들 초기화 ##########

        delta_for_layers = [[] for i in range(self.number_of_layers)]
        for iter in range(self.number_of_layers):
            delta_for_layers[iter] = np.zeros((self.number_of_training_data, self.number_of_nodes[iter+1])) # (트레이닝 입력 갯수)x(각 뉴런별 노드 갯수)행렬인 델타를 만듦.
        print(f'delta_for_layers는 {delta_for_layers}')

        print(f'\nnumber_of_nodes는 {self.number_of_nodes}\nnumber_of_weight_for_layers는 {self.weight_for_layers}\n')
        ########## 계속 루프를 돌면서 웨이트,proactivation,y추정값 업데이트! ##########

        for update in range(loop_number) :
            delta_sum = [[0] for i in range(self.number_of_layers)]
            for level in range(self.number_of_layers):
                for later in range(self.number_of_nodes[-(level+1)]):
                    for front in range(self.number_of_nodes[-(level + 2)]):
                        gradient = 0
                        for n in range(self.number_of_training_data):
                            gradient = 0

                            if level == 0 : #맨 마지막 뉴런의 델타
                                #print(f'if 문이 실행되었습니다. level = {level}\n')
                                for n in range(self.number_of_training_data):
                                    delta_for_layers[-(level+1)][n][later] = -(self.y_[n][later] - self.y_est_final[n][later]) * self.y_est_final[n][later] * (1 - self.y_est_final[n][later])
                                    gradient += (self.y_est_for_layers[-2][n][front]) * delta_for_layers[-(level+1)][n][later]
                                # n번 루프 다 돌았고,
                                self.weight_for_layers[-(level+1)][front][later] = self.weight_for_layers[-(level+1)][front][later] - ((self.lr) * gradient)
                                #print(f'delta_for_layers는 {delta_for_layers}')


                            elif level == self.number_of_layers-1 : #맨 처음 뉴런의 델타
                                #print(f'elif 문이 실행되었습니다. level = {level}\n')
                                for j in range(self.number_of_nodes[2]):
                                    tmp = 0
                                    tmp += (self.weight_for_layers[1][later][j]) * delta_for_layers[1][n][j]
                                delta_sum[level] = tmp
                                delta_for_layers[0][n][later] = self.y_est_for_layers[0][n][later] * (1 - self.y_est_for_layers[0][n][later]) * delta_sum[level]
                                gradient += (self.x_[n][front]) * delta_for_layers[0][n][later]
                                # n번 루프 다 돌았고,
                                self.weight_for_layers[0][front][later] = self.weight_for_layers[0][front][later] - ((self.lr) * gradient)
                                #print(f'delta_for_layers는 {delta_for_layers}')

                            else : #중간 뉴런들의 델타
                                #print(f'else 문이 실행되었습니다. level = {level}\n')
                                for j in range(self.number_of_nodes[-(level)]):
                                    tmp = 0
                                    tmp += (self.weight_for_layers[-(level)][later][j]) * delta_for_layers[-(level)][n][j]
                                delta_sum[level] = tmp
                                delta_for_layers[-(level+1)][n][later] = self.y_est_for_layers[-(level+1)][n][later] * (1 - self.y_est_for_layers[-(level+1)][n][later]) * delta_sum[level]
                                gradient += (self.y_est_for_layers[-(level+2)][n][front]) * delta_for_layers[-(level+1)][n][later]
                                # n번 루프 다 돌았고,
                                self.weight_for_layers[-(level+1)][front][later] = self.weight_for_layers[-(level+1)][front][later] - ((self.lr) * gradient)
                                #print(f'delta_for_layers는 {delta_for_layers}')

                #print(f'{self.number_of_layers-(level)}번째 웨이트 벡터는 {self.weight_for_layers[-(level + 1)]}')





            for iter in range(self.number_of_layers):  # 뉴런 갯수만큼 루프 돌면서 웨이트, proactivation, y추정값 전부 초기화
                if iter == 0:  # 첫번째 뉴런의 proactivation, y추정값
                    self.proactivation_for_layers[iter] = np.dot(self.x_, self.weight_for_layers[
                        iter])  ########## 첫번째 proactivation (a벡터) 초기화 ############
                    self.y_est_for_layers[iter] = self.sigmoid(
                        self.proactivation_for_layers[iter])  ########## 첫번째 y_est (y추정값 벡터) 초기화 ############
                elif iter == self.number_of_layers - 1:  # 마지막 뉴런의 proactivation, y추정값
                    self.a_final = np.dot(self.y_est_for_layers[self.number_of_layers - 2], self.weight_for_layers[
                        self.number_of_layers - 1])  ########## 마지막 proactivation (a벡터) 초기화 ############
                    self.y_est_final = self.sigmoid(self.a_final)  ########## 마지막 y_est (y추정값 벡터) 초기화 ############
                else:  # 각 뉴런의 proactivation, y추정값
                    self.proactivation_for_layers[iter] = np.dot(self.y_est_for_layers[iter - 1],
                                                                 self.weight_for_layers[
                                                                     iter])  ########## 첫번째 proactivation (a벡터) 초기화 ############
                    self.y_est_for_layers[iter] = self.sigmoid(
                        self.proactivation_for_layers[iter])  ########## 첫번째 y_est (y추정값 벡터) 초기화 ############

            self.cost = sum(self.y_ - self.y_est_final) ** 2  ########## cost 초기화 ############
            #print(f'a_final는 {self.a_final}\ny_est_final는 {self.y_est_final}\ncost는 {self.cost}')

            #print(f'a_는 {self.a_}\ny_est는 {self.y_est}\ncost는 {self.cost}')

            #print(f'업데이트된 cost는 {self.cost}')
            #print(f'w_ki = {self.w_ki}')



    def show(self):
        print(f'x_ = {self.x_}\n')
        print(f'y_ = {self.y_}\n')
        print(f'y_est = {self.y_est_final}\n')
        print(f'cost = {self.cost}\n')

slp = Perceptron()
slp.initialize()
slp.feed_forward_and_gradient_back_propagation()
slp.show()

