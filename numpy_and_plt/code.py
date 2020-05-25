import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("data/", one_hot=True)

print('train dataset:', mnist.train.images.shape, mnist.train.labels.shape)
print('test dataset:', mnist.test.images.shape, mnist.test.labels.shape)
print('validation dataset:', mnist.validation.images.shape, mnist.validation.labels.shape)
fig = plt.figure(figsize=(7,7))

for i in range(25):
    subplot=fig.add_subplot(5,5,i+1)
    mnist_img = np.reshape(mnist.train.images[i+10],[28,28])
    subplot.imshow(mnist_img, cmap='Greys')
    subplot.set_xticks([]) #이거 해주면 화면상에 이상한 격자들 없앨 수 있음.
    subplot.set_yticks([])

plt.show()
