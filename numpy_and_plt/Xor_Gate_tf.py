# -*- coding:utf -8 -*-

import tensorflow as tf
import numpy as np
lr = 0.5

t_data = [[0,0],[0,1],[1,0],[1,1]]
label = [[0],[1],[1],[0]]
t_data = np.array(t_data,dtype=np.float32)
label = np.array(label,dtype=np.float32)

X=tf.placeholder(tf.float32, [None,2])
Y=tf.placeholder(tf.float32, [None,1])

W1=tf.Variable(tf.random_normal([2, 2]))
b1=tf.Variable(tf.random_normal([2]))

O1 = tf.nn.sigmoid(tf.matmul(X,W1)+b1)
#=================================================
# layer2, 2 input 1 output
#=================================================
W2=tf.Variable(tf.random_normal([2, 1]))
b2=tf.Variable(tf.random_normal([1]))

Y_ = tf.nn.sigmoid(tf.matmul(O1,W2)+b2)

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
            print(step,sess.run(cost,feed_dict={X:t_data, Y:label}),sess.run(W1))
    h,c,a = sess.run([Y_,predicted,accuracy],feed_dict ={X:t_data,Y:label})
    print("\nHypothesis: ", h, "\nCorrect: ", c, "\nAccuracy: ", a)
    print(sess.run(W1), sess.run(b1))  # 여기 위에선 W와 b에 무엇을 넣어준다 이런것도 없다. 근데 업데이트(학습)이 될수 있었던 이유는 train세션의 cost부분에서 W와 b를 알아서 찾아내어서 학습을 시킴.
    print(sess.run(W2), sess.run(b2))


