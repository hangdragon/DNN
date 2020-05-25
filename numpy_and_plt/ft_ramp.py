# -*- coding : utf -8 -*-

import tensorflow as tf
import numpy as np
lr = 0.5 #learning rate
#=================================================
# training data & place holder
#=================================================
t_data = [[0,0],[0,1],[1,0],[1,1]] #2차원 행렬을 만들기 위한 재료이자 트레이닝 입력 데이터
label = [[0],[0],[0],[1]] #2차원 행렬을 만들기 위한 재료이자 라벨
t_data = np.array(t_data, dtype=np.float32) #넘파이로 ndarray를 만들어 줄때, dtype을 지정해줄 수 도 있다.
label = np.array(label, dtype=np.float32)
X=tf.placeholder(tf.float32, [None,2])# none 행 2열의 플레이스 홀더를 지정해줌.
# =================================================
# Weight and Bias
# =================================================
W=tf.Variable(tf.random_normal([2, 1]), name='weight')
b=tf.Variable(tf.random_normal([1]), name='bias')
# =================================================
# Operation graph
# =================================================
Y_ = tf.sigmoid(tf.matmul(X,W)+b)

# =================================================
# Training and verification graph
# =================================================
cost = -tf.reduce_mean(Y*tf.log(Y_)+(1-Y)*tf.log(1-Y_))
train = tf.train.GradientDescentOptimizer(learning_rate=lr).minimize(cost)
predicted = tf.cast(Y_>0.5, dtype=tf.float32) # tf.cast는 map함수의 역할 + 뒤에 걸어준 dtype으로 각 원소를 캐스팅을 수행한다. 여기서는 반올림 역할로 쓰였다.
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted,Y),dtype=tf.float32)) #tf.equal은 두 벡터의 원소를 하나하나 비교하며 같으면 T,다르면 F를 반환하는 벡터를 반환한다.
#tf.reduce_mean은 해당 벡터에 대한 평균을 반환한다. 추가적인 아규먼트로 0이나 1을 써주면 열,행별로 평균을 계산한다.
# =================================================
# Run Session
# =================================================
with tf.Session() as sess: #sess객체를 이렇게 부르겠다. 뿐만아니라 해당 블럭이 끝나면 세션은 자동으로 종료가 된다.
   sess.run(tf.global_variables_initializer())
   for step in range(10001):
      sess.run(train,feed_dict={X:t_data, Y:label})
      if step % 100 == 0:
           print(step, sess.run(cost,feed_dict={X:t_data, Y:label}),sess.run(W))
   h,c,a=sess.run([Y_, predicted, accuracy], feed_dict={X:t_data, Y:label})
   print("\nHypothesis: ", h, "\nCorrect: ", c, "\nAccuracy: ", a)
   print(sess.run(W),sess.run(b))
