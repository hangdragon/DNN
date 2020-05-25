# -*- coding:utf-8 -*-

"""

0. architecture 정하기. layer 갯수, 각 노드 갯수, 트레이닝 데이터 셋의 원소의 갯수
1. t_data , label 2차원 텐서로 초기화, dtype들은 무조건 정해주고, 초기화 해준다. 얘내는 처음에는 넘파이임
X,Y를 텐서 플레이스 홀더로 해준다.
"""
import tensorflow as tf
import numpy as np
lr = 0.01

t_data =[[0,0],[0,1],[1,0],[1,1]] # 트레이닝 데이터 셋 원소 갯수 x 입력 노드 갯수
label = [[0],[0],[0],[1]] # 트레이닝 데이터 셋 원소 갯수 x 출력 노드 갯수
t_data = np.array(t_data,dtype=np.float32)
label = np.array(label,dtype=np.float32)

#t_data와 label을 2차원 넘파이 행렬로 받고, 각각을 dtype을 정하고 통일하여 초기화 해줬다. 이 다음은 이것들을 2차원 텐서로 해줘야함

X = tf.placeholder(tf.float32,[None,2],name = 't_data') #tensorflow에서 변하는 것이면 , variable로 하고, 변하지 않는 것이라면 placeholder로 하자.
Y = tf.placeholder(tf.float32,[None,1],name = 'label')


W = tf.Variable(tf.random_normal([2,1]),name = 'weight') #앞 레이어 노드 갯수 x 뒷 레이어 노드 갯수
b = tf.Variable((tf.random_normal((1,))),name = 'bias')

Y_ = tf.nn.relu(X@W +b) #하나의 뉴런을 거친다음 나온 추정값.

cost = tf.reduce_sum(((Y-Y_)**2))
#cost = -tf.reduce_mean(Y*tf.log(Y_)+(1-Y)*tf.log(1-Y_))
train = tf.train.GradientDescentOptimizer(learning_rate=lr).minimize(cost)
predicted = tf.cast(Y_>0.5, dtype=tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted,Y),dtype=tf.float32))
# =================================================
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(10001):
        sess.run(train,feed_dict={X:t_data,Y:label})
        if step % 100 == 0:
            print(step,sess.run(cost,feed_dict={X:t_data, Y:label}),sess.run(W))
    h,c,a = sess.run([Y_,predicted,accuracy],feed_dict ={X:t_data,Y:label})
    print("\nHypothesis: ", h, "\nCorrect: ", c, "\nAccuracy: ", a)
    print(sess.run(W), sess.run(b))  # 여기 위에선 W와 b에 무엇을 넣어준다 이런것도 없다. 근데 업데이트(학습)이 될수 있었던 이유는 train세션의 cost부분에서 W와 b를 알아서 찾아내어서 학습을 시킴.


