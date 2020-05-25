# -*- coding : utf- 8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Import MNIST data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("/tmp/data/", one_hot=True) # one_hot = True를 해주게 되면 본래 label은 0부너 10까지의 정수인데 이것을 (10,) 넘파이 행렬로 바꿔줌. 원 핫 인코딩 해줌.


print("훈련 이미지 :",  mnist.train.images.shape)
print("훈련 라벨:",  mnist.train.labels.shape)
print("테스트 이미지 : ", mnist.test.images.shape)
print("테스트 라벨 : ", mnist.test.labels.shape)
print("검증 이미지 : ", mnist.validation.images.shape)
print("검증 라벨 : ", mnist.validation.labels.shape)
print('\n')


mnist_idx = 100


print('[label]')
print('one-hot vector label = ', mnist.train.labels[mnist_idx])
print('number label = ', np.argmax(mnist.train.labels[mnist_idx])) #np.argmax는 컨테이너에서 가장 큰 요소의 인덱스 값을 반환한다
print('\n')

print('[image]')

for index, pixel in enumerate(mnist.train.images[mnist_idx]):
    if index % 28 == 0:
        print('\n')
    else:
        print("%10f" % pixel, end="")
print('\n')

print(f'image 각각의 차원 : {mnist.train.images[mnist_idx].shape}, image의 타입 : {type(mnist.train.images[mnist_idx])}')
print(mnist.train.num_examples)
plt.figure(figsize=(3, 3))
image = np.reshape(mnist.train.images[mnist_idx], [28, 28])
#image = mnist.train.images[mnist_idx].reshape(28,28)
plt.imshow(image)
plt.show()