# -*- coding : utf -8 -*-

import tensorflow as tf
import numpy as np

class Perceptron_tf :

    def architecture(self):
        ########## layer의 갯수(layer_number)입력 ###########
        self.number_of_layers = int(input('원하시는 레이어의 갯수를 입력하세요(1이상인 정수입니다!) : '))
        self.number_of_nodes = [[] for i in range(self.number_of_layers + 1)]  # SLP이면 x,y , DLP이면 x,h1,y,,,의 노드 갯수를 담으려고 만든 리스트.
        # x,h1,y에서 x는 트레이닝 데이터의 노드들 갯수. h1는 hidden layer1에 대한 노드들 갯수. y는 출력 데이터 노드들 갯수를 의미한다.
        # number_of_nodes라는 리스트 안에는 각 단계별 노드 갯수인 '스칼라'값이 들어간다. number_of_nodes의 길이는 number_of_layers의 +1!

        ##########  히든 레이어 갯수 및 입력,출력,히든 레이어 각각의 노드 갯수들 초기화 ############
        if self.number_of_layers == 1:
            print('{}를 선택하셨습니다.\n트레이닝 데이터, 출력 데이터 노드의 갯수를 각각 입력하세요.'.format('SLP'))
            for i in range(len(self.number_of_nodes)):
                if i == 0:
                    self.number_of_nodes[i] = int(input('$트레이닝 데이터 노드 갯수 >>>'))-1
                elif i == self.number_of_layers:
                    self.number_of_nodes[i] = int(input('$출력 데이터 노드 갯수 >>>'))

        elif self.number_of_layers == 2:
            print('{}를 선택하셨습니다.\n트레이닝 데이터, 히든 레이어 노드, 출력 데이터 노드의 갯수를 각각 입력하세요.'.format('DLP'))
            for i in range(len(self.number_of_nodes)):
                if i == 0:
                    self.number_of_nodes[i] = int(input('$트레이닝 데이터 노드 갯수 >>>'))-1
                elif i == self.number_of_layers:
                    self.number_of_nodes[i] = int(input('$출력 데이터 노드 갯수 >>>'))
                else:
                    self.number_of_nodes[i] = int(input('$히든 레이어 노드 갯수 >>>'))-1

        else:
            print('히든 레이어가 {}개인 {}를 선택하셨습니다.'.format(self.number_of_layers - 1, 'MLP'))
            print('\n트레이닝 데이터, 히든 레이어들의 노드, 출력 데이터 노드의 갯수를 각각 입력하세요.')
            for i in range(len(self.number_of_nodes)):
                if i == 0:
                    self.number_of_nodes[i] = int(input('$트레이닝 데이터 노드 갯수 >>>'))-1
                elif i == self.number_of_layers:
                    self.number_of_nodes[i] = int(input('$출력 데이터 노드 갯수 >>>'))
                else:
                    self.number_of_nodes[i] = int(input(f'$히든 레이어{i}의 노드 갯수 >>>'))-1
            print(f'\n노드 갯수들은 다음과 같습니다 {self.number_of_nodes}')

        ############트레이닝 데이터의 갯수 입력#############
        self.number_of_training_data = int(input('\n원하시는 트레이닝 데이터의 갯수를 입력하세요 : '))  # ex) (0,0),(0,1),(1,0),(1,1)이면 n = 4

    def __init__(self):  # 생성자는 멤버 변수들의 선언 및 아키텍처 단계를 수행한다.

        self.number_of_layers = 0  # layer 갯수
        self.number_of_nodes = []  # 선택한 아키텍처에 대한 레이어별 노드 갯수들
        self.number_of_training_data = 0  # training data 갯수이자 label 갯수
        self.architecture()  # architecture 멤버 함수를 실행하여 위의 세개의 변수 값을 초기화!

        self.number_of_input_node = self.number_of_nodes[0]
        self.number_of_output_node = self.number_of_nodes[-1]
        self.t_data = np.zeros((self.number_of_training_data, self.number_of_input_node)) # 입력 트레이닝 데이터
        self.x_ = tf.placeholder(tf.float32,[None,self.number_of_input_node],name = 't_data')
        self.label = np.zeros((self.number_of_training_data, self.number_of_output_node))  # 출력 트레이닝 데이터(레이블들)
        self.y_ = tf.placeholder(tf.float32, [None, self.number_of_output_node], name='label')

        self.weight_for_layers = [[] for i in range(self.number_of_layers)]  # 전체 레이어의 갯수만큼 각각에 해당하는 웨이트 벡터들을 담을 리스트
        self.bias_for_layers = [[] for i in range(self.number_of_layers)]  # 전체 레이어의 갯수만큼 각각에 해당하는 바이어스들을 담을 리스트
        self.y_est_for_layers = [[] for i in range(self.number_of_layers)]  # 전체 레이어의 갯수만큼 각각에 해당하는 y 벡터들을 담을 리스트

        self.y_est_final = []
        self.cost = 0  # 최종 에러함수(비용함수)

        ###########learning rate 입력############
        self.lr = float(input('\n원하시는 learning rate를 입력해주세요 : '))
        self.select_ftn = None

    def initialize(self):
        ########## 트레이닝 데이터들 (x벡터들) 입력 ############
        print('\n트레이닝 데이터를 하나씩 입력하세요. (입력 예시 : (0,0)이면 >>>0 0)\n')
        for i in range(self.number_of_training_data):
            self.t_data[i] = list(map(float, input(f'요소의 갯수가 {self.number_of_input_node}개인 {(i + 1)}번째 트레이닝 데이터 입력 >>').strip().split()))
        self.t_data = np.array(self.t_data,dtype=np.float32)
        #self.x_ = tf.placeholder(tf.float32,[None,self.number_of_input_node],name = 't_data')

        ########## 레이블들 (y벡터들) 입력 ############
        print('\n라벨들을 하나씩 입력하세요. (입력 예시 : (1,2)이면 >>>1 2)\n')
        for j in range(self.number_of_training_data):
            self.label[j] = list(map(float, input(f'요소의 갯수가 {self.number_of_output_node}인 {(j + 1)}번째 레이블 입력 >>').strip().split()))
        self.label = np.array(self.label, dtype=np.float32)
        #self.y_ = tf.placeholder(tf.float32, [None, self.number_of_output_node], name='label')

        ########### activation ftn을 sigmoid로 할지 relu로 할지 결정하는 곳 ###########
        print('\nweight vector들을 초기화 하기전에 먼저 activation ftn를 뭘로할지 선탁해야합니다.')
        self.select_ftn = input('activation ftn을 선택하세요.\nex) sigmoid를 쓰고싶다면 sigmoid, relu를 쓰고싶다면 relu, leaky_relu를 쓰고싶다면 leaky_relu.\n\n>>>')
        if self.select_ftn == 'sigmoid':
            ########## sigmoid-> 웨이트벡터들(w벡터들)을 가우시안으로 초기화 ############
            for iter in range(len(self.weight_for_layers)):
                print('#######{}번째 layer의 weight 초기화#######'.format(iter + 1))  # 각 뉴런마다의 웨이트벡터를 초기화 해주기 위함
                print(f'\n제 {iter + 1}번째 뉴런의 웨이트 벡터의 요소의 갯수는 {self.number_of_nodes[iter] * self.number_of_nodes[iter + 1]}개 입니다.')
                print(f'{iter + 1}번째 뉴런의 웨이트 벡터들을 가우시안 분포를 사용한 Xavier방법으로 초기화 하겠습니다.')
                self.weight_for_layers[iter] = tf.Variable(tf.random_normal((self.number_of_nodes[iter], self.number_of_nodes[iter + 1]),0,np.sqrt(2/((self.number_of_nodes[iter]+self.number_of_nodes[iter + 1])))))
                self.bias_for_layers[iter] = tf.Variable(tf.random_normal([self.number_of_nodes[iter + 1]], 0, np.sqrt(2 / ((self.number_of_nodes[iter] + self.number_of_nodes[iter + 1])))))
                if iter == 0 :
                    self.y_est_for_layers[0] = tf.nn.sigmoid(tf.matmul(self.x_, self.weight_for_layers[0]) + self.bias_for_layers[0])
                else:
                    self.y_est_for_layers[iter] = tf.nn.sigmoid(tf.matmul(self.y_est_for_layers[iter-1], self.weight_for_layers[iter]) + self.bias_for_layers[iter])

        elif self.select_ftn == 'relu':
            ########## relu-> 웨이트벡터들(w벡터들)을 He Initialization으로 초기화 ############
            for iter in range(len(self.weight_for_layers)):
                print('#######{}번째 layer의 weight 초기화#######'.format(iter + 1))  # 각 뉴런마다의 웨이트벡터를 초기화 해주기 위함
                print(f'\n제 {iter + 1}번째 뉴런의 웨이트 벡터의 요소의 갯수는 {self.number_of_nodes[iter] * self.number_of_nodes[iter + 1]}개 입니다.')
                print(f'{iter + 1}번째 뉴런의 웨이트 벡터들을 He Initialization으로 초기화 하겠습니다.')
                self.weight_for_layers[iter] = tf.Variable(tf.random_normal((self.number_of_nodes[iter], self.number_of_nodes[iter + 1]),0,np.sqrt(2/self.number_of_nodes[iter])))
                self.bias_for_layers[iter] = tf.Variable(tf.random_normal([self.number_of_nodes[iter + 1]], 0, np.sqrt(2 / self.number_of_nodes[iter])))
                if iter == 0 :
                    self.y_est_for_layers[0] = tf.nn.relu(tf.matmul(self.x_, self.weight_for_layers[0]) + self.bias_for_layers[0])
                elif iter == self.number_of_layers-1 : #마지막 뉴런에서는 늘 sigmoid로 해주기 위함
                    self.y_est_for_layers[iter] = tf.sigmoid(tf.matmul(self.y_est_for_layers[iter - 1], self.weight_for_layers[iter]) + self.bias_for_layers[iter])
                else:
                    self.y_est_for_layers[iter] = tf.nn.relu(tf.matmul(self.y_est_for_layers[iter-1], self.weight_for_layers[iter]) + self.bias_for_layers[iter])

        elif self.select_ftn == 'leaky_relu':
            ########## relu-> 웨이트벡터들(w벡터들)을 He Initialization으로 초기화 ############
            for iter in range(len(self.weight_for_layers)):
                print('#######{}번째 layer의 weight 초기화#######'.format(iter + 1))  # 각 뉴런마다의 웨이트벡터를 초기화 해주기 위함
                print(f'\n제 {iter + 1}번째 뉴런의 웨이트 벡터의 요소의 갯수는 {self.number_of_nodes[iter] * self.number_of_nodes[iter + 1]}개 입니다.')
                print(f'{iter + 1}번째 뉴런의 웨이트 벡터들을 He Initialization으로 초기화 하겠습니다.')
                self.weight_for_layers[iter] = tf.Variable(tf.random_normal((self.number_of_nodes[iter], self.number_of_nodes[iter + 1]),0, np.sqrt(2 / self.number_of_nodes[iter])))
                self.bias_for_layers[iter] = tf.Variable(tf.random_normal([self.number_of_nodes[iter + 1]], 0, np.sqrt(2 / self.number_of_nodes[iter])))
                if iter == 0 :
                    self.y_est_for_layers[0] = tf.nn.leaky_relu(tf.matmul(self.x_, self.weight_for_layers[0]) + self.bias_for_layers[0],0.0001)
                elif iter == self.number_of_layers-1 : #마지막 뉴런에서는 늘 sigmoid로 해주기 위함
                    self.y_est_for_layers[iter] = tf.sigmoid(tf.matmul(self.y_est_for_layers[iter - 1], self.weight_for_layers[iter]) + self.bias_for_layers[iter])
                else:
                    self.y_est_for_layers[iter] = tf.nn.leaky_relu(tf.matmul(self.y_est_for_layers[iter-1], self.weight_for_layers[iter]) + self.bias_for_layers[iter],0.0001)
        self.y_est_final = self.y_est_for_layers[-1]
        self.cost = tf.reduce_sum(((self.y_ - self.y_est_final) ** 2))

    def feed_forward_and_gradient_back_propagation(self,loop_number=20000) :

        train = tf.train.GradientDescentOptimizer(learning_rate=self.lr).minimize(self.cost)
        predicted = tf.cast(self.y_est_final > 0.5, dtype=tf.float32)
        accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, self.y_), dtype=tf.float32))
        # =================================================
        with tf.Session() as sess: #이 블럭 안에서만 세션이 유효하다. 이 블럭 나가게되면 세션값들의 데이터엔 접근할 수 없다.
            sess.run(tf.global_variables_initializer())
            for step in range(loop_number):
                sess.run(train, feed_dict={self.x_: self.t_data, self.y_: self.label})
                if step % 100 == 0:
                    print(step, sess.run(self.cost, feed_dict={self.x_: self.t_data, self.y_: self.label}), sess.run(self.weight_for_layers))
            h, c, a = sess.run([self.y_, predicted, accuracy], feed_dict={self.x_: self.t_data, self.y_: self.label})
            print("\nHypothesis: ", h, "\nCorrect: ", c, "\nAccuracy: ", a)
            print(sess.run(self.weight_for_layers), sess.run(self.bias_for_layers))  # 여기 위에선 W와 b에 무엇을 넣어준다 이런것도 없다. 근데 업데이트(학습)이 될수 있었던 이유는 train세션의 cost부분에서 W와 b를 알아서 찾아내어서 학습을 시킴.
            self.weight_for_layers = sess.run(self.weight_for_layers) #세션 종료전에 self.weight를 세선 런한 값으로 초기화 해줘야함. 이거 안해주면 학습 전의 이상한 웨이트가 들어가버림
            self.bias_for_layers = sess.run(self.bias_for_layers) #바이어스도 마찬가지!

    def testing(self):
        sigma = float(input('가우시안 노이즈의 표준편차를 입력해주세요(0을 입력하면 binary 분포를 따릅니다) : '))
        test_x = np.zeros((1, self.number_of_input_node)) # 입력 트레이닝 데이터
        for i in range(len(test_x[0])):
            test_x[0][i] = np.random.randint(2) + np.random.normal(0,sigma)# 0 또는 1에 대해 equivalent하게 할당.(binary)
            # 한편, 입력받은 표준편차를 바탕으로 평균이 0 이고 분산이 sigma^2인 가우시안 확률변수를 더해줬음.
        test_x = np.array(test_x,dtype=np.float32)
        ####### 수렴된 w벡터들을 가지고 퍼셉트론안에서 계속 절차를 돌린 후, y_test값을 얻어내면 끝! #######
        if self.select_ftn == 'sigmoid':
            ########## sigmoid-> 웨이트벡터들(w벡터들)을 가우시안으로 초기화 ############
            for iter in range(len(self.weight_for_layers)):
                if iter == 0 :
                    self.y_est_for_layers[0] = tf.nn.sigmoid(tf.matmul(test_x, self.weight_for_layers[0]) + self.bias_for_layers[0])
                else:
                    self.y_est_for_layers[iter] = tf.nn.sigmoid(tf.matmul(self.y_est_for_layers[iter-1], self.weight_for_layers[iter]) + self.bias_for_layers[iter])

        elif self.select_ftn == 'relu':
            ########## relu-> 웨이트벡터들(w벡터들)을 He Initialization으로 초기화 ############
            for iter in range(len(self.weight_for_layers)):
                if iter == 0 :
                    self.y_est_for_layers[0] = tf.nn.relu(tf.matmul(test_x, self.weight_for_layers[0]) + self.bias_for_layers[0])
                else:
                    self.y_est_for_layers[iter] = tf.nn.relu(tf.matmul(self.y_est_for_layers[iter-1], self.weight_for_layers[iter]) + self.bias_for_layers[iter])

        elif self.select_ftn == 'leaky_relu':
            ########## relu-> 웨이트벡터들(w벡터들)을 He Initialization으로 초기화 ############
            for iter in range(len(self.weight_for_layers)):
                if iter == 0 :
                    self.y_est_for_layers[0] = tf.nn.leaky_relu(tf.matmul(test_x, self.weight_for_layers[0]) + self.bias_for_layers[0])
                else:
                    self.y_est_for_layers[iter] = tf.nn.leaky_relu(tf.matmul(self.y_est_for_layers[iter-1], self.weight_for_layers[iter]) + self.bias_for_layers[iter])
        self.y_est_final = self.y_est_for_layers[-1]
        predicted = tf.cast(self.y_est_final > 0.5, dtype=tf.float32)
        self.cost = tf.reduce_sum(((self.y_ - self.y_est_final) ** 2))

        sess = tf.Session()
        sess.run(tf.global_variables_initializer())
        print(f'test데이터 {test_x}를 넣었을때 추정값 y는 {sess.run(predicted,feed_dict={self.x_:test_x})}')

perceptron = Perceptron_tf()
perceptron.initialize()
perceptron.feed_forward_and_gradient_back_propagation()
perceptron.testing()