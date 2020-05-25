#-*- coding: utf-8 -*

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
lr = 0.5 #learning rate
#=================================================
# training data & place holder
#=================================================
t_data = [[0,0],[0,1],[1,0],[1,1]]
label = [[0],[0],[0],[1]]
t_data = np.array(t_data , dtype =np.float32)
label = np.array (label, dtype =np.float32)


#=================================================
# layer1, 2 input 2 output
#=================================================
X= tf.placeholder (tf.float32, [None,2])
Y= tf.placeholder (tf.float32, [None,1])
W1= tf.Variable (tf.random_normal ([2, 2]), name='weight1')
b1= tf.Variable (tf.random_normal ([2]), name='bias1')
O1 = tf.sigmoid(tf.matmul (X,W1)+ b1)
#=================================================
# layer2, 2 input 1 output
#=================================================
W2=tf.Variable (tf.random_normal ([2, 1]), name='weight2')
b2=tf.Variable (tf.random_normal ([1]), name='bias2')
Y_ =tf.sigmoid (tf.matmul (O1,W2)+ b2)
# =================================================
# Weight and Bias
# =================================================
W= tf.Variable(tf.random_normal ([2, 1]), name='weight')
b= tf.Variable(tf.random_normal ([1]), name='bias')
# =================================================
# Operation graph
# =================================================
Y_=tf.sigmoid(tf.matmul(X,W)+b)
# =================================================
# Training and verification graph
# =================================================
cost = -tf.reduce_mean (Y*tf.log(Y_)+(1-Y)*tf.log(1-Y_))
train = tf.train.GradientDescentOptimizer(learning_rate=lr ).minimize(cost)
predicted = tf.cast (Y_>0.5,dtype =tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted,Y),dtype =tf.float32))
# =================================================
# Run Session
# =================================================
with tf.Session () as sess :
    sess.run(tf.global_variables_initializer())
    for step in range(10001):
        sess.run(train,feed_dict = {X:t_data , Y:label})
        if step % 100 == 0:
            print(step,sess.run(cost,feed_dict={X:t_data , Y:label}),sess.run(W))
    h,c,a = sess.run ([Y_, predicted, accuracy],feed_dict={X:t_data , Y:label})
    print("\nHypothesis : ", h, "\nCorrect : ", c, "\nAccuracy : ",a)
    print(sess.run(W),sess.run(b))