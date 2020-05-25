# -*- coing:utf-8 -*-
import tensorflow as tf
# =================================================
# read MNIST DB
# =================================================
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("data/", one_hot=True)

import numpy as np
import cv2 #opencv 모듈을 불러오기 위해서는 import opencv가 아니라 import cv2를 하여야한다.

n1 = np.random.randint(10,200,[256,256,3]) #유색의 랜덤한 그림을 만든다.
#n1 = np.zeros([1792,828,3]) #828 x 1792짜리 jpg파일을 만들 틀.
#n1[:][:][0] = np.random.randint(10,200,[1792,828])


image=cv2.imread("9D194DF8-01FE-4E4E-8AE0-522C77143077.jpg",-1) #cv2.imread(디렉토리 상의 파일 이름, 그 파일을 어떤식으로 읽을 것인지 모드 정하기) -> ndarray 반환
print(f'image의 타입 : {type(image)}, image의 shape : {image.shape}, image의 값 : {image}')
tmp= cv2.namedWindow('window',cv2.WINDOW_NORMAL)
#cv2.imshow('window',n1); cv2.waitKey(0)
modified_image = {}

modified_image['up_down_invert'] = image[::-1]
modified_image['half_row'] = image[:len(image)//2]
modified_image['column_row'] = image.transpose()[:len(image.transpose())//2].transpose()
print(f'modified_image의 타입 : {type(modified_image["up_down_invert"])}, modified_image의 shape : {modified_image["up_down_invert"].shape}, modified_image의 값 : {modified_image["up_down_invert"]}')
#print(f'modified_image의 타입 : {type(modified_image["up_down_invert"])}, modified_image의 shape : {modified_image["up_down_invert"].shape}, modified_image의 값 : {modified_image["up_down_invert"]}')
#print(f'modified_image의 타입 : {type(modified_image["up_down_invert"])}, modified_image의 shape : {modified_image["up_down_invert"].shape}, modified_image의 값 : {modified_image["up_down_invert"]}')


#window = cv2.namedWindow('Koala', cv2.WINDOW_AUTOSIZE) #WINDOW_AUTOSIZE
#cv2.imshow(window, image); cv2.waitKey(0);
image = -image; #근데 이것도 몇비트 사진인가에 따라 다른거 아닌가? 아니였음.. 그림이 24비트 사진이라 해도 이건 무조건 255였네.
#cv2.imshow('Inverted Koala',image); cv2.waitKey(0);
#cv2.imwrite("inverted_sw.jpg", image)

for i in range(50): #애니 매이션 만들기
    if (i%10 == 0) or (i%10 == 1) or(i%10 == 2) or(i%10 == 3) or(i%10 == 4): #반은 흑백, 반은 컬러 처리
        n1 = np.random.randint(np.random.randint(0,20,[1]), np.random.randint(100,300,[1]), [256, 256])
    else :
        n1 = np.random.randint(np.random.randint(0,20,[1]), np.random.randint(100,300,[1]), [256, 256,3])

    cv2.imwrite('muneo.jpg',n1)
    image = cv2.imread('muneo.jpg', -1)
    cv2.imshow('Random_Animation',image)
    cv2.waitKey(100)
window = cv2.namedWindow('Number_Animation', cv2.WINDOW_NORMAL)
for i in range(5): #애니 매이션 만들기
    cv2.imshow(window,mnist.test.images[np.random.randint(0,10000)])
    cv2.waitKey(1000)


cv2.destroyAllWindows()

#column_half = n1.transpose()[:len(n1.transpose())//2]