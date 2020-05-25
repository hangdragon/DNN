# -*- coding: utf-8 -*-

import cv2

img_color = cv2.imread('jjukkumi.png',cv2.IMREAD_) # IMREAD_COLOR 투명도 정보를 가진 알파채널을 무시한채, 그냥 컬러로 읽음.
#참고로 cv2.imread('읽어올 파일 이름' , flags)인데, flags 에는 cv2.IMREAD_COLOR , cv2.IMREAD_GRAYSACLE , cv2.IMREAD_UNCHANGED가 있다. UNCHANGEDS는 알파채널 + 유색
#imread를 통해 불러온 이미지의 타입은 ndarray이다.


'''imread 함수는 이미지 파일을 해당 flag(읽어들일 모드)에 대하여 불러와서 그 값을 리턴한다.'''
cv2.namedWindow('sangwa1') #윈도우 선언

cv2.imshow('sangwa1', img_color) # 윈도우에 ndarray 이미지 파일을 넣기



cv2.waitKey(0) # 사용자로부터 키보드 입력을 무한히 대기, 요 안에 1을 입력하면 0.001초이다. 1초를 만들려면 1000을 넣어줘야함.

'''cv2.waitKey 1개당 n개의 윈도우를 띄우는 1 phase가 실행됨.'''

img_gray = cv2.cvtColor(img_color,cv2.COLOR_BGR2GRAY)

cv2.namedWindow('sangwa2')

cv2.imshow('sangwa2',img_gray)

cv2.waitKey(0)

cv2.imwrite('new_sangwa.jpg',img_gray) # 해당 flag를 적용한 ndarray 이미지 파일을 new_sangwa라는 파일로 저
cv2.destroyAllWindows() # 이미지 파일을 위한 모든 윈도우를 해제한다.



