# -*- coding : utf-8 -*-

import tensorflow as tf
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
X = tf.placeholder(tf.float32, [None, 784])  # data
Y = tf.placeholder(tf.float32, [None, 10])  # label
# =================================================
# layer 1 processing
# =================================================
W1 = tf.Variable(tf.random_normal([784, 392], stddev=0.01))
L1 = tf.nn.relu(tf.matmul(X, W1))
# =================================================
# layer 2 processing
# =================================================
W2 = tf.Variable(tf.random_normal([392, 10], stddev=0.01))
L2 = tf.matmul(L1, W2)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=L2, labels=Y))
optimizer = tf.train.AdamOptimizer(0.001).minimize(cost)
# train_step=tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
# =================================================
# Data feed
# =================================================
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# =================================================
# mini batch operation, batchsize=100
# =================================================
batch_size = 100
total_batch = int(mnist.train.num_examples / batch_size) # 550개의 배
for epoch in range(15):
	total_cost = 0
	for i in range(total_batch): # 1 epoch당 100 size의 배치 1개를 각각 550번 돌림.
		batch_xs, batch_ys = mnist.train.next_batch(batch_size)
		_, cost_val = sess.run([optimizer, cost], feed_dict={X: batch_xs, Y: batch_ys}) # optimizer값을 _로 해준 이유는 저 값을 굳이 출력 할 필요가 없기 떄문 ,
		#그리고 optimizer와 cost 각각을 sess.run할 것을 한번에 해주기 위함(일일이 feed_dict하여 데이터 먹여주는 것도 귀찮아.. 한번에 해보자)
		total_cost += cost_val #배치 1개 돌리고 1 업데이트 하였을때 코스트 값이 cost_val인데, 그 것을 550개를 더해줘야한다. 1epoch별 코스트는 total_cost이고 그 값은 총 배치 갯수로 나눠줘야함
	print('Epoch:', '%04d' % (epoch + 1), 'Avg. cost = ', '{:.3f}'.format(total_cost / total_batch))
print('Optimization done!')
# =================================================
# Verification
# =================================================
correct_prediction = tf.equal(tf.argmax(L2, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={X: mnist.test.images, Y: mnist.test.labels}))
