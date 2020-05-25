# -*- coding : utf - 8 -*-

import cv2
import numpy as np
from scipy import signal as sig

image = cv2.imread('9D194DF8-01FE-4E4E-8AE0-522C77143077.jpg', cv2.IMREAD_UNCHANGED)
image = cv2.resize(image, dsize=(256,256),interpolation=cv2.INTER_LINEAR) # 그냥 다운 샘플링 하였음. 근데 그냥 다운 샘플링 하게되면 에일리어싱이 생겨서, 미리 다운샘플링 전에
#앤티 에일리어싱 필터를 써야한다. #다운 샘플링 -> 이미지 자체의 사이즈(크기)를 줄인 것임. 글고 이것은 이미지의 크기만 (픽셀 수만) 줄인것이지, 필터를 통과한건 아님. 통과하는것은 아래의 컨벌루션으로!



"""2D 컨볼루션을 해보자. 아래는 필터임"""
h = np.ones((3,3))/9

"""2D 컨볼루션을 해보자."""
row = image.shape[0]
col = image.shape[1]
test_builtin = 0
if(test_builtin==0):
    for i in range(row-3):
        print(i)
        for j in range(col-3):
            sum = 0
            for k in range(3):
                for l in range(3):
                    sum = sum + image[i+k][j+l]*h[k][l]
            image[i][j] = sum

cv2.namedWindow('Koala', cv2.WINDOW_AUTOSIZE)  # WINDOW_AUTOSIZE
cv2.imshow('Koala', image);
cv2.waitKey(0);

#image = 255 - image;

#cv2.imshow('Inverted Koala', image);
#cv2.waitKey(0);
#cv2.imwrite('new_new_sangwa.jpg', image)
cv2.destroyAllWindows()

