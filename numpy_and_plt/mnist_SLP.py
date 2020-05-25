# -*- coding : utf-8 -*-

import tensorflow as tf
import numpy as np
# =================================================
# read MNIST DB
# =================================================
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("data/", one_hot=True)
print('train dataset:', mnist.train.images.shape, mnist.train.labels.shape)
print('test dataset:', mnist.test.images.shape, mnist.test.labels.shape)
print('validation dataset:', mnist.validation.images.shape, mnist.validation.labels.shape)
# =================================================
# placeholder to feed data to graph 28x28=784
# =================================================
x = tf.placeholder(tf.float32, [None, 784])  # data
y = tf.placeholder(tf.float32, [None, 10])  # label
# =================================================
# Weight and Bias
# =================================================
W = tf.Variable(tf.random_normal([784, 10], stddev=0.01))
# =================================================
# Operational graph
# =================================================
y_ = tf.nn.softmax(tf.matmul(x, W))
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y * tf.log(y_), reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
# =================================================
# Data feed
# =================================================
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
# =================================================
# mini batch operation, batchsize=100
# =================================================
for i in range(2000):
	batch_xs, batch_ys = mnist.train.next_batch(100) #100개씩 images와 labels를 묶어준 튜플이다. 첫번째 튜플의 shape은 (100,784)이고 , 두번째 튜플의 shape은 (100,10)이다.
	#한편 , mnist.train.next_batch(뭐시기)는 튜플이다!!!! ndarray가 아니다!!
	sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})
	if i % 100 == 0 :
		print(f'x : {batch_xs} , y : {batch_ys}\nx의 shape : {batch_xs.shape} , y의 shape : {batch_ys.shape}\nmnist.train.next_batch(100)의 len : {len(mnist.train.next_batch(100))}') ;print('mnist.train.next_batch(100)의 정체를 알아내려 한다.\n과연 55000개의 이미지들중 몇번째에서 몇번째를 100개씩 묶은 것일까?\n');print(f'mnist.train.next_batch(100)[0]은 mnist.train.images의 몇번째 원소일까?\n');print(f'>>> {np.where(mnist.train.images == batch_xs[0])}')
# =================================================
# Verification
# =================================================
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1)) #tf.argmax(컨테이너,1)은 2차원 컨테이너에서 행마다 비교해가며 그 행에서 가장 큰 원소가 있는 인덱스를 반환한다.
#원핫 인코딩의 컨테이너일 경우, 0~9까지의 해당 숫자를 말해준다. #즉.. tf.argmax(y,1)혹은 np.argmax()는 원핫 인코딩 된 것을 디코딩 하기 위함이다.! 0~9까지의 숫자를 도로 반환받기 위함이다.
print(f' y : {sess.run(y,feed_dict={x: mnist.test.images, y: mnist.test.labels})}, y_ : {sess.run(y_,feed_dict={x: mnist.test.images, y: mnist.test.labels})}')
print(f'tf.argmax(y,1) : {sess.run(tf.argmax(y,1),feed_dict={x: mnist.test.images, y: mnist.test.labels})} ,tf.argmax(y_,1) : {sess.run(tf.argmax(y_,1),feed_dict={x: mnist.test.images, y: mnist.test.labels})}')
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels}))
